"""Placement routes."""

from flask import Blueprint, request, jsonify
from database import db
from models import Placement, Student, Company
from flask_jwt_extended import jwt_required, get_jwt_identity

placement_bp = Blueprint('placement', __name__, url_prefix='/api/placements')

@placement_bp.route('', methods=['GET'])
def get_placements():
    """Get all placements."""
    placements = Placement.query.all()
    return jsonify([
        {
            'id': p.id,
            'student_name': f"{p.student.first_name} {p.student.last_name}",
            'company_name': p.company.company_name,
            'job_title': p.job_title,
            'salary': p.salary,
            'status': p.status
        } for p in placements
    ]), 200

@placement_bp.route('/<int:placement_id>', methods=['GET'])
def get_placement(placement_id):
    """Get placement by ID."""
    placement = Placement.query.get(placement_id)
    if not placement:
        return jsonify({'message': 'Placement not found'}), 404
    
    return jsonify({
        'id': placement.id,
        'student_id': placement.student_id,
        'company_id': placement.company_id,
        'job_title': placement.job_title,
        'salary': placement.salary,
        'job_type': placement.job_type,
        'status': placement.status,
        'description': placement.description
    }), 200

@placement_bp.route('', methods=['POST'])
@jwt_required()
def create_placement():
    """Create a new placement record."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    placement = Placement(
        student_id=data.get('student_id'),
        company_id=data.get('company_id'),
        job_title=data.get('job_title'),
        salary=data.get('salary'),
        job_type=data.get('job_type'),
        description=data.get('description')
    )
    
    db.session.add(placement)
    db.session.commit()
    
    return jsonify({'message': 'Placement created successfully', 'placement_id': placement.id}), 201
