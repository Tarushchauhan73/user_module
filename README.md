# Django User Management REST API

A RESTful API built using **Python, Django, and Django REST Framework** to manage users. The API supports creating, retrieving, updating, and soft-deleting user records using class-based views.

## Features

- Create new users.
- Retrieve all active, non-deleted users.
- Retrieve a single user by ID.
- Update user details using PUT and PATCH.
- Soft-delete users without permanently removing database records.
- Validate user data using serializers.
- Automatically track creation and update timestamps.
- Prevent duplicate usernames and email addresses.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- REST API
- VS Code

## Project Structure

```text
user_api_project/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md
```
## screenshot 
<img width="1440" height="900" alt="Screenshot 2026-10-13 at 11 47 30 AM" src="https://github.com/user-attachments/assets/c0ff5094-c095-4842-bc45-32f7c0279467" />
<img width="1440" height="900" alt="Screenshot 2026-10-13 at 12 03 45 PM" src="https://github.com/user-attachments/assets/9c8781dc-6e74-4b3f-983d-4882090d0e31" />
<img width="1440" height="900" alt="Screenshot 2026-10-13 at 11 46 55 AM" src="https://github.com/user-attachments/assets/de04aa34-4d85-43b3-9be5-136f58a6f8f4" />
<img width="1440" height="900" alt="Screenshot 2026-10-13 at 12 14 13 PM" src="https://github.com/user-attachments/assets/afb12b44-ca6c-43c8-8bbf-fbf009a61305" />





## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd user_api_project
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install django djangorestframework
```

### 5. Run database migrations

```bash
python manage.py makemigrations users
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/users/` | Retrieve all non-deleted users |
| POST | `/api/users/` | Create a new user |
| GET | `/api/users/<id>/` | Retrieve a user by ID |
| PUT | `/api/users/<id>/` | Update a user's details |
| PATCH | `/api/users/<id>/` | Partially update a user |
| DELETE | `/api/users/<id>/` | Soft-delete a user |

Replace `<id>` with the actual user ID.

## User Model

The User model includes the following fields:

| Field | Description |
|---|---|
| `id` | Automatically generated primary key |
| `username` | Unique username |
| `first_name` | User's first name |
| `last_name` | User's last name |
| `email` | Unique email address |
| `phone` | Contact number |
| `is_active` | Indicates whether the account is active |
| `is_deleted` | Indicates whether the user has been soft-deleted |
| `created_at` | Record creation timestamp |
| `updated_at` | Last update timestamp |

## Example Requests

### Create a user

**POST** `/api/users/`

```json
{
  "username": "tarush",
  "first_name": "Tarush",
  "last_name": "Chauhan",
  "email": "tarush@example.com",
  "phone": "9876543210"
}
```

### Retrieve all users

**GET** `/api/users/`

Returns a list of users who have not been soft-deleted.

### Retrieve one user

**GET** `/api/users/1/`

Returns the user whose ID is `1`, if the user exists and has not been soft-deleted.

### Update a user

**PUT** `/api/users/1/`

```json
{
  "username": "tarush_updated",
  "first_name": "Tarush",
  "last_name": "Chauhan",
  "email": "tarush.updated@example.com",
  "phone": "9876543210"
}
```

PUT generally requires all required editable fields to be supplied.

### Partially update a user

**PATCH** `/api/users/1/`

```json
{
  "first_name": "UpdatedName"
}
```

Only the supplied field is changed.

### Soft-delete a user

**DELETE** `/api/users/1/`

The API sets `is_deleted` to `true` instead of permanently deleting the database record. The user is then excluded from normal list and detail queries.

## Soft Delete vs Hard Delete

**Soft delete:** The record remains in the database, with `is_deleted=True`.

**Hard delete:** The database record is permanently removed.

This project uses soft deletion to preserve records for possible auditing or recovery. Recovery is not exposed as an API endpoint in the current implementation.

## Testing

You can test the API using:

- The Django REST Framework browsable API in your web browser.
- Postman.
- `curl`.

Example:

```bash
curl http://127.0.0.1:8000/api/users/
```

## Learning Outcomes

- Understanding Django models and database migrations.
- Creating serializers with Django REST Framework.
- Implementing class-based API views.
- Configuring URL routing.
- Handling GET, POST, PUT, PATCH, and DELETE requests.
- Implementing soft deletion.
- Testing REST API endpoints.

## Future Improvements

- Add authentication and permissions.
- Add pagination and search.
- Add user recovery after soft deletion.
- Write automated API tests.
- Add API documentation using Swagger or OpenAPI.

## Author

**Tarush Chauhan**

GitHub: [Tarushchauhan73](https://github.com/Tarushchauhan73)
