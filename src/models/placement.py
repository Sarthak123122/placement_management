"""Placement model."""

from database import db
from datetime import datetime

class Placement(db.Model):
    __tablename__ = 'placements'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float)
    job_type = db.Column(db.String(50))  # Full-time, Intern, etc.
    status = db.Column(db.String(20), default='pending')  # pending, selected, rejected, accepted
    offer_date = db.Column(db.DateTime)
    join_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    student = db.relationship('Student', backref='placements')
    company = db.relationship('Company', backref='placements')
