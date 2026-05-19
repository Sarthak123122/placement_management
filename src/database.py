"""Database initialization and configuration."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    """Initialize the database."""
    from models import User, Student, Company, Placement
    db.create_all()
