import os
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv

from .models import db

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///altus.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Firebase Admin
    if not firebase_admin._apps:
        # Assuming the credentials file is in the backend root directory
        cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), '..', 'firebase_credentials.json'))
        firebase_admin.initialize_app(cred)

    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
