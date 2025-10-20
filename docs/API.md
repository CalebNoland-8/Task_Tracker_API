# API Documentation

## Overview

The Task Tracker API provides a RESTful interface for managing tasks with user authentication.

## Base URL

```
http://localhost:8000
```

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints:

1. Register a new user or login to get an access token
2. Include the token in the Authorization header: `Authorization: Bearer <token>`

## Response Format

All responses are in JSON format.

### Success Response

```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "completed": false,
  "priority": "medium",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": null,
  "user_id": 1
}
```

### Error Response

```json
{
  "detail": "Error message"
}
```

## Endpoints

### Authentication Endpoints

#### Register User

**POST** `/api/v1/auth/register`

Create a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2024-01-01T00:00:00"
}
```

#### Login

**POST** `/api/v1/auth/login`

Login with username and password to get access token.

**Request Body:** (application/x-www-form-urlencoded)
```
username=johndoe
password=securepassword123
```

**Response:** `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Task Endpoints

All task endpoints require authentication.

#### Get All Tasks

**GET** `/api/v1/tasks/`

Get all tasks for the authenticated user.

**Query Parameters:**
- `skip` (optional): Number of tasks to skip (default: 0)
- `limit` (optional): Maximum number of tasks to return (default: 100)

**Headers:**
```
Authorization: Bearer <token>
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the task tracker API",
    "completed": false,
    "priority": "high",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": null,
    "user_id": 1
  }
]
```

#### Get Task by ID

**GET** `/api/v1/tasks/{task_id}`

Get a specific task by ID.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the task tracker API",
  "completed": false,
  "priority": "high",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": null,
  "user_id": 1
}
```

**Error Response:** `404 Not Found`
```json
{
  "detail": "Task not found"
}
```

#### Create Task

**POST** `/api/v1/tasks/`

Create a new task.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "title": "Complete project",
  "description": "Finish the task tracker API",
  "priority": "high",
  "completed": false
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the task tracker API",
  "completed": false,
  "priority": "high",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": null,
  "user_id": 1
}
```

#### Update Task

**PUT** `/api/v1/tasks/{task_id}`

Update an existing task.

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:** (all fields optional)
```json
{
  "title": "Updated title",
  "description": "Updated description",
  "priority": "low",
  "completed": true
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Updated title",
  "description": "Updated description",
  "completed": true,
  "priority": "low",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-02T00:00:00",
  "user_id": 1
}
```

#### Delete Task

**DELETE** `/api/v1/tasks/{task_id}`

Delete a task.

**Headers:**
```
Authorization: Bearer <token>
```

**Response:** `204 No Content`

**Error Response:** `404 Not Found`
```json
{
  "detail": "Task not found"
}
```

## Status Codes

- `200 OK`: Request successful
- `201 Created`: Resource created successfully
- `204 No Content`: Request successful, no content to return
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required or failed
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation error

## Data Models

### Task

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | integer | - | Unique identifier (auto-generated) |
| title | string | Yes | Task title (1-200 characters) |
| description | string | No | Task description |
| completed | boolean | No | Task completion status (default: false) |
| priority | string | No | Task priority: "low", "medium", or "high" (default: "medium") |
| created_at | datetime | - | Creation timestamp (auto-generated) |
| updated_at | datetime | - | Last update timestamp (auto-generated) |
| user_id | integer | - | Owner user ID (auto-assigned) |

### User

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | integer | - | Unique identifier (auto-generated) |
| email | string | Yes | User email (must be valid email) |
| username | string | Yes | Username (3-50 characters, unique) |
| password | string | Yes | Password (minimum 8 characters) |
| is_active | boolean | - | Account active status (default: true) |
| is_superuser | boolean | - | Superuser status (default: false) |
| created_at | datetime | - | Registration timestamp (auto-generated) |
| updated_at | datetime | - | Last update timestamp (auto-generated) |

## Examples

See the main README.md for curl examples and usage patterns.
