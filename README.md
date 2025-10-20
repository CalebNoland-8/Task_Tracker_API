# Task Tracker API

A RESTful API for managing tasks, built with FastAPI, PostgreSQL, Docker, and JWT authentication.

## Features

- 🚀 **FastAPI**: Modern, fast web framework for building APIs
- 🔐 **JWT Authentication**: Secure user authentication and authorization
- 🐘 **PostgreSQL**: Robust relational database
- 🐳 **Docker**: Containerized application for easy deployment
- ✅ **CRUD Operations**: Complete task management functionality
- 📝 **API Documentation**: Auto-generated interactive API docs
- 🧪 **Testing**: Comprehensive test suite with pytest

## Project Structure

```
Task_Tracker_API/
├── src/
│   ├── __init__.py
│   ├── config.py              # Application configuration
│   ├── auth/                  # Authentication modules
│   │   ├── __init__.py
│   │   ├── dependencies.py    # Auth dependencies
│   │   └── security.py        # Password hashing & JWT
│   ├── database/              # Database configuration
│   │   ├── __init__.py
│   │   └── connection.py      # DB connection & session
│   ├── models/                # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── task.py           # Task model
│   │   └── user.py           # User model
│   ├── routes/                # API routes
│   │   ├── __init__.py
│   │   ├── auth.py           # Auth endpoints
│   │   └── tasks.py          # Task endpoints
│   ├── schemas/               # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── task.py           # Task schemas
│   │   └── user.py           # User schemas
│   ├── services/              # Business logic (future)
│   │   └── __init__.py
│   └── utils/                 # Utility functions (future)
│       └── __init__.py
├── tests/                     # Test files
│   ├── __init__.py
│   ├── test_main.py          # Main tests
│   ├── unit/                 # Unit tests
│   │   └── __init__.py
│   └── integration/          # Integration tests
│       └── __init__.py
├── docs/                      # Documentation (future)
├── scripts/                   # Utility scripts (future)
├── alembic/                   # Database migrations (to be initialized)
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose configuration
├── alembic.ini               # Alembic configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 15+ (or use Docker)
- Docker & Docker Compose (optional but recommended)

### Installation

#### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/CalebNoland-8/Task_Tracker_API.git
cd Task_Tracker_API
```

2. Create a `.env` file from the example:
```bash
cp .env.example .env
```

3. Update the `.env` file with your configurations

4. Start the application with Docker Compose:
```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`

#### Option 2: Local Development

1. Clone the repository:
```bash
git clone https://github.com/CalebNoland-8/Task_Tracker_API.git
cd Task_Tracker_API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

5. Update the `.env` file with your database configuration

6. Initialize the database:
```bash
# If using Alembic for migrations
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

7. Run the application:
```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
```

## API Documentation

Once the application is running, you can access:

- **Interactive API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get access token

### Tasks

- `GET /api/v1/tasks/` - Get all tasks (requires authentication)
- `GET /api/v1/tasks/{task_id}` - Get a specific task
- `POST /api/v1/tasks/` - Create a new task
- `PUT /api/v1/tasks/{task_id}` - Update a task
- `DELETE /api/v1/tasks/{task_id}` - Delete a task

### Health Check

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint

## Usage Examples

### Register a New User

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=securepassword123"
```

### Create a Task

```bash
curl -X POST "http://localhost:8000/api/v1/tasks/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project",
    "description": "Finish the task tracker API",
    "priority": "high",
    "completed": false
  }'
```

### Get All Tasks

```bash
curl -X GET "http://localhost:8000/api/v1/tasks/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_main.py

# Run with verbose output
pytest -v
```

## Database Migrations

This project uses Alembic for database migrations:

```bash
# Initialize Alembic (already done)
alembic init alembic

# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Development

### Code Formatting

```bash
# Format code with black
black .

# Lint with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

### Environment Variables

Key environment variables (see `.env.example` for complete list):

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Secret key for JWT token generation
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_ORIGINS`: CORS allowed origins

## Deployment

### Docker Deployment

The application includes Docker configuration for easy deployment:

1. Build the image:
```bash
docker build -t task-tracker-api .
```

2. Run with Docker Compose:
```bash
docker-compose up -d
```

### Production Considerations

- Change `SECRET_KEY` to a strong, random value
- Set `DEBUG=False` in production
- Use environment-specific `.env` files
- Configure proper CORS origins
- Set up SSL/TLS certificates
- Use a production-grade WSGI server (uvicorn with workers)
- Implement rate limiting
- Set up proper logging and monitoring

## Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migration**: Alembic
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Validation**: Pydantic
- **Testing**: pytest
- **Containerization**: Docker & Docker Compose

## Roadmap

- [x] Basic project structure
- [x] User authentication with JWT
- [x] CRUD operations for tasks
- [x] Docker configuration
- [ ] Database migrations with Alembic
- [ ] Enhanced task features (due dates, tags, categories)
- [ ] User profile management
- [ ] Task sharing and collaboration
- [ ] Email notifications
- [ ] File attachments
- [ ] Advanced filtering and search
- [ ] API rate limiting
- [ ] Comprehensive logging
- [ ] CI/CD pipeline
- [ ] Production deployment guide

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please open an issue on GitHub.
