from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/check', methods=['GET'])
def health_check():
    return {
        'status': 'ok',
        'message': 'User management service is running'
    }  

@user_bp.route('/', methods=['GET'])
def get_users():
    mongo = request.blueprint.app.mongo
    users = list(mongo.db.users.find())
    for u in users:
        u['_id'] = str(u['_id'])  # Convert ObjectId to string
    return jsonify(users)

@user_bp.route('/create', methods=['POST'])
def create_user():
    mongo = request.blueprint.app.mongo
    data = request.json
    result = mongo.db.users.insert_one({'name': data['name']})
    return jsonify({'id': str(result.inserted_id)}), 201

@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    mongo = request.blueprint.app.mongo
    data = request.json
    result = mongo.db.users.update_one(
        {'_id': mongo.db.ObjectId(user_id)},
        {'$set': {'name': data['name']}}
    )
    return jsonify({'modified_count': result.modified_count})

@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    mongo = request.blueprint.app.mongo
    result = mongo.db.users.delete_one({'_id': mongo.db.ObjectId(user_id)})
    return jsonify({'deleted_count': result.deleted_count})
