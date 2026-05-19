# Python to React JSX Conversion Notes

## Overview
This document details the conversion of the Placement Management System from Python Flask backend to a React frontend with JSX components.

## Files Converted

### 1. **app.py → App.jsx**
   - Converted Flask application factory to React root component
   - Flask blueprints → React Router routes
   - Replaced Flask context with React Context API providers
   - Database initialization → useEffect hook with initialization logic

### 2. **config.py → Config.js**
   - Configuration class → ES6 JavaScript class with static methods
   - Environment variables → process.env access
   - Timedelta objects → Milliseconds for JavaScript
   - Added API endpoints mapping for consistency

### 3. **database.py → Database.js**
   - SQLAlchemy → Fetch API wrapper service
   - Database session → Singleton service instance
   - Models initialization → API endpoint requests
   - Added error handling and token management

### 4. **main.py → index.jsx**
   - Flask app execution → React DOM rendering
   - Entry point logic → ReactDOM.createRoot
   - Hot Module Replacement support for development

## Additional Files Created

### Context Providers (State Management)
- **AuthContext.jsx** - Authentication state and login/logout operations
- **StudentContext.jsx** - Student data management
- **CompanyContext.jsx** - Company data management
- **PlacementContext.jsx** - Placement data management

### Services
- **Database.js** - API communication layer with CRUD operations

### Components
- **ProtectedRoute.jsx** - Route protection for authenticated users

## Architecture Changes

### Before (Flask)
```
Flask App
├── Routes (Blueprints)
├── Models (SQLAlchemy)
├── Database (SQLAlchemy Session)
└── Config
```

### After (React)
```
React App
├── Routes (React Router)
├── Contexts (State Management)
├── Services (API Layer)
├── Components (UI)
└── Config
```

## Key Conversions

| Python | React |
|--------|-------|
| Flask app | React component with Router |
| Blueprints | Route components |
| SQLAlchemy models | REST API endpoints |
| Configuration class | JavaScript class with static methods |
| Database session | Service singleton |
| Timedelta | Milliseconds |
| Request/response handling | Fetch API |
| Context manager | React Context API |

## Dependencies Required

```json
{
  "react": "^18.0.0",
  "react-dom": "^18.0.0",
  "react-router-dom": "^6.0.0"
}
```

## Environment Variables

Create a `.env` file in the root directory:

```env
REACT_APP_API_BASE_URL=http://localhost:5000/api
REACT_APP_DATABASE_URL=http://localhost:5000
REACT_APP_SECRET_KEY=dev-secret-key-change-in-production
REACT_APP_JWT_SECRET_KEY=jwt-secret-key
```

## Migration Guide

1. **Replace Python backend routes** with REST API endpoints that match the Config.ENDPOINTS structure
2. **Update component page files** (Login, Dashboard, etc.) to use the provided contexts
3. **Ensure backend API** responds to the documented endpoints
4. **Configure proxy** in package.json for development if API runs on different port

## Notes

- All async operations use async/await pattern
- Error handling implemented with try-catch blocks
- Token-based authentication with localStorage
- Automatic logout on 401 responses
- Debug mode tied to NODE_ENV
