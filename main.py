from flask import Flask
from user_management.routes import user_management_bp
from config import Config

app = Flask(__name__)

# Attach MongoDB to the Flask app context
app.db = Config.db

# Register Blueprint with base URL
app.register_blueprint(user_management_bp, url_prefix="/user-management")

@app.route('/')
def home():
    return "Flask + MongoDB API is running!"

if __name__ == '__main__':
    app.run(debug=True)
