import os
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv

from .models import db

load_dotenv()

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    template_dir = os.path.join(BASE_DIR, 'frontend', 'templates')
    static_dir = os.path.join(BASE_DIR, 'frontend', 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
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
    from .views import views as views_blueprint
    
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(views_blueprint)

    @app.context_processor
    def inject_firebase_config():
        return dict(
            FIREBASE_API_KEY=os.getenv('FIREBASE_API_KEY'),
            FIREBASE_AUTH_DOMAIN=os.getenv('FIREBASE_AUTH_DOMAIN'),
            FIREBASE_PROJECT_ID=os.getenv('FIREBASE_PROJECT_ID')
        )

    return app
