"""Student routes."""

from flask import Blueprint, request, jsonify
from database import db
from models import Student, User
from flask_jwt_extended import jwt_required, get_jwt_identity

student_bp = Blueprint('student', __name__, url_prefix='/api/students')

@student_bp.route('', methods=['GET'])
def get_students():
    """Get all students."""
    students = Student.query.all()
    return jsonify([
        {
            'id': s.id,
            'name': f"{s.first_name} {s.last_name}",
            'roll_number': s.roll_number,
            'department': s.department,
            'cgpa': s.cgpa,
            'is_placed': s.is_placed
        } for s in students
    ]), 200

@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student by ID."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    
    return jsonify({
        'id': student.id,
        'name': f"{student.first_name} {student.last_name}",
        'roll_number': student.roll_number,
        'department': student.department,
        'cgpa': student.cgpa,
        'branch': student.branch,
        'phone': student.phone,
        'is_placed': student.is_placed
    }), 200

@student_bp.route('', methods=['POST'])
@jwt_required()
def create_student():
    """Create a new student."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    student = Student(
        user_id=current_user_id,
        roll_number=data.get('roll_number'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        department=data.get('department'),
        cgpa=data.get('cgpa'),
        branch=data.get('branch'),
        phone=data.get('phone')
    )
    
    db.session.add(student)
    db.session.commit()
    
    return jsonify({'message': 'Student created successfully', 'student_id': student.id}), 201
