# Placement Management System - Project Structure

## Directory Layout

```
placement_management/
├── src/
│   ├── main.py                 # Application entry point
│   ├── app.py                  # Flask app factory
│   ├── config.py               # Configuration settings
│   ├── database.py             # Database initialization
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User model (admin, student, company, coordinator)
│   │   ├── student.py         # Student model
│   │   ├── company.py         # Company model
│   │   └── placement.py       # Placement model
│   └── routes/
│       ├── __init__.py
│       ├── auth.py            # Authentication endpoints
│       ├── student.py         # Student endpoints
│       ├── company.py         # Company endpoints
│       └── placement.py       # Placement endpoints
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_student.py
│   ├── test_company.py
│   └── test_placement.py
├── docs/
│   ├── PROJECT_STRUCTURE.md   # This file
│   ├── API_DOCUMENTATION.md   # API endpoints documentation
│   └── SETUP_GUIDE.md         # Setup and installation guide
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # Project README
```

## Module Descriptions

### Models
- **User**: Base user model with roles (admin, student, company, coordinator)
- **Student**: Student profile with academic details
- **Company**: Company profile for recruitment
- **Placement**: Placement records linking students to companies

### Routes
- **auth**: User registration and login endpoints
- **student**: CRUD operations for student profiles
- **company**: CRUD operations for company profiles
- **placement**: CRUD operations for placement records

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token

### Students
- `GET /api/students` - Get all students
- `GET /api/students/<id>` - Get student details
- `POST /api/students` - Create new student

### Companies
- `GET /api/companies` - Get all companies
- `GET /api/companies/<id>` - Get company details
- `POST /api/companies` - Create new company

### Placements
- `GET /api/placements` - Get all placements
- `GET /api/placements/<id>` - Get placement details
- `POST /api/placements` - Create new placement

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Set up environment variables: `cp .env.example .env`
3. Run the application: `python src/main.py`
4. Access API at `http://localhost:5000`
