"""Routes package."""

from .auth import auth_bp
from .student import student_bp
from .company import company_bp
from .placement import placement_bp

__all__ = ['auth_bp', 'student_bp', 'company_bp', 'placement_bp']
