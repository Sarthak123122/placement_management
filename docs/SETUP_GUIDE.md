# Setup Guide - Placement Management System

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Sarthak123122/placement_management.git
cd placement_management
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your settings
```

### 5. Run the Application
```bash
python src/main.py
```

The application will be available at `http://localhost:5000`

## Project Structure

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed information.

## Testing

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src/
```

## Development

### Running in Development Mode
```bash
FLASK_ENV=development python src/main.py
```

### Using Gunicorn (Production-like)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 src.app:app
```

## Database

### Create Database
The database is automatically created when you run the application for the first time.

### Reset Database
```bash
# Delete the database file
rm placement.db

# Run the application to recreate
python src/main.py
```

## Common Issues

### ModuleNotFoundError
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`

### Database Locked Error
- Close any other instances of the application
- Delete `placement.db` and restart

### Port Already in Use
Change the port in `src/main.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Deployment

For production deployment, see Docker configuration and deployment guides in the docs folder.

## Support

For issues or questions, please create an issue on GitHub.
