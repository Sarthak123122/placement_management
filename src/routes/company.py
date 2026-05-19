"""Company routes."""

from flask import Blueprint, request, jsonify
from database import db
from models import Company
from flask_jwt_extended import jwt_required, get_jwt_identity

company_bp = Blueprint('company', __name__, url_prefix='/api/companies')

@company_bp.route('', methods=['GET'])
def get_companies():
    """Get all verified companies."""
    companies = Company.query.filter_by(is_verified=True).all()
    return jsonify([
        {
            'id': c.id,
            'company_name': c.company_name,
            'industry': c.industry,
            'location': c.location,
            'website': c.website
        } for c in companies
    ]), 200

@company_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id):
    """Get company by ID."""
    company = Company.query.get(company_id)
    if not company:
        return jsonify({'message': 'Company not found'}), 404
    
    return jsonify({
        'id': company.id,
        'company_name': company.company_name,
        'industry': company.industry,
        'location': company.location,
        'website': company.website,
        'contact_person': company.contact_person,
        'contact_email': company.contact_email,
        'description': company.description
    }), 200

@company_bp.route('', methods=['POST'])
@jwt_required()
def create_company():
    """Create a new company."""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    company = Company(
        user_id=current_user_id,
        company_name=data.get('company_name'),
        industry=data.get('industry'),
        location=data.get('location'),
        website=data.get('website'),
        contact_person=data.get('contact_person'),
        contact_email=data.get('contact_email'),
        contact_phone=data.get('contact_phone'),
        description=data.get('description')
    )
    
    db.session.add(company)
    db.session.commit()
    
    return jsonify({'message': 'Company created successfully', 'company_id': company.id}), 201
