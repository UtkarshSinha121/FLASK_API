from flask import Blueprint
from user_management.users import user_bp
# from users import user_bp

user_management_bp = Blueprint('user_management', __name__)

user_management_bp.register_blueprint(user_bp, url_prefix='/users')