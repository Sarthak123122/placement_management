"""Application factory for Flask app."""

from flask import Flask
from config import Config
from database import db, init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        init_db()
    
    # Register blueprints
    from routes import auth_bp, student_bp, company_bp, placement_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(placement_bp)
    
    return app
