# Employee Management API

A Django RESTful API for managing employees, departments, performance reviews, and attendance. Built with Django, Django REST Framework, PostgreSQL, and Swagger for API documentation.

## Features

- CRUD operations for Employees, Departments, Performance, and Attendance
- Token-based Authentication
- Swagger/OpenAPI Documentation

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/employee_project.git
cd employee_project
```

### 2. Clone the repository

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure database
Make sure PostgreSQL is running and create database
```bash
CREATE DATABASE employee_db;
```
Update .env

### 4. Run migrations and create a superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run server 
```bash
python manage.py runserver
```

## API Documentation
Swagger docs are available at http://127.0.0.1:8000/swagger/
