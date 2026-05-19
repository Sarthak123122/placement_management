# API Documentation - Placement Management System

## Base URL
```
http://localhost:5000/api
```

## Authentication
All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

## Endpoints

### Authentication

#### Register User
- **Endpoint**: `POST /auth/register`
- **Description**: Register a new user
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password",
    "role": "student"  // admin, student, company, coordinator
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "message": "User registered successfully",
    "user_id": 1
  }
  ```

#### Login User
- **Endpoint**: `POST /auth/login`
- **Description**: Login and get JWT token
- **Request Body**:
  ```json
  {
    "username": "john_doe",
    "password": "secure_password"
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "message": "Login successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "user_id": 1,
    "role": "student"
  }
  ```

### Students

#### Get All Students
- **Endpoint**: `GET /students`
- **Description**: Retrieve all students
- **Response**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "roll_number": "2210992266",
      "department": "Computer Science",
      "cgpa": 8.5,
      "is_placed": true
    }
  ]
  ```

#### Get Student by ID
- **Endpoint**: `GET /students/<id>`
- **Description**: Retrieve specific student details
- **Response**: `200 OK`
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "roll_number": "2210992266",
    "department": "Computer Science",
    "cgpa": 8.5,
    "branch": "Engineering",
    "phone": "9876543210",
    "is_placed": true
  }
  ```

#### Create Student
- **Endpoint**: `POST /students`
- **Description**: Create new student profile (Requires JWT)
- **Request Body**:
  ```json
  {
    "roll_number": "2210992266",
    "first_name": "John",
    "last_name": "Doe",
    "department": "Computer Science",
    "cgpa": 8.5,
    "branch": "Engineering",
    "phone": "9876543210"
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "message": "Student created successfully",
    "student_id": 1
  }
  ```

### Companies

#### Get All Companies
- **Endpoint**: `GET /companies`
- **Description**: Retrieve all verified companies
- **Response**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "company_name": "Tech Corp",
      "industry": "Information Technology",
      "location": "Bangalore",
      "website": "https://techcorp.com"
    }
  ]
  ```

#### Get Company by ID
- **Endpoint**: `GET /companies/<id>`
- **Description**: Retrieve specific company details
- **Response**: `200 OK`
  ```json
  {
    "id": 1,
    "company_name": "Tech Corp",
    "industry": "Information Technology",
    "location": "Bangalore",
    "website": "https://techcorp.com",
    "contact_person": "Jane Smith",
    "contact_email": "recruit@techcorp.com",
    "description": "Leading IT company..."
  }
  ```

#### Create Company
- **Endpoint**: `POST /companies`
- **Description**: Create new company profile (Requires JWT)
- **Request Body**:
  ```json
  {
    "company_name": "Tech Corp",
    "industry": "Information Technology",
    "location": "Bangalore",
    "website": "https://techcorp.com",
    "contact_person": "Jane Smith",
    "contact_email": "recruit@techcorp.com",
    "contact_phone": "9876543210",
    "description": "Leading IT company..."
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "message": "Company created successfully",
    "company_id": 1
  }
  ```

### Placements

#### Get All Placements
- **Endpoint**: `GET /placements`
- **Description**: Retrieve all placement records
- **Response**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "student_name": "John Doe",
      "company_name": "Tech Corp",
      "job_title": "Software Engineer",
      "salary": 600000,
      "status": "selected"
    }
  ]
  ```

#### Get Placement by ID
- **Endpoint**: `GET /placements/<id>`
- **Description**: Retrieve specific placement details
- **Response**: `200 OK`
  ```json
  {
    "id": 1,
    "student_id": 1,
    "company_id": 1,
    "job_title": "Software Engineer",
    "salary": 600000,
    "job_type": "Full-time",
    "status": "selected",
    "description": "Job description here..."
  }
  ```

#### Create Placement
- **Endpoint**: `POST /placements`
- **Description**: Create new placement record (Requires JWT)
- **Request Body**:
  ```json
  {
    "student_id": 1,
    "company_id": 1,
    "job_title": "Software Engineer",
    "salary": 600000,
    "job_type": "Full-time",
    "description": "Job description here..."
  }
  ```
- **Response**: `201 Created`
  ```json
  {
    "message": "Placement created successfully",
    "placement_id": 1
  }
  ```

## Error Responses

### 400 Bad Request
```json
{
  "message": "Missing required fields"
}
```

### 401 Unauthorized
```json
{
  "message": "Invalid credentials"
}
```

### 404 Not Found
```json
{
  "message": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "message": "Internal server error"
}
```
