# Student_management_System(Backend)
A backend REST API for managing students and courses using Django,Django REST Framework,MongoDB (MongoEngine) and JWT Authentication.  
Django REST API for student and course management using MongoDB and JWT authentication.
## Tech Stack:
- Django
- Django REST Framework
- MongoDB
- JWT Authentication
## JWT Authentication:
JWT authentication secures APIs using token-based access, enabling stateless login, role-based permissions, and secure communication without server-side sessions to connect JWT Authentication using Postman & Thunder Client 
## Features:
- JWT Authentication (Login & Refresh)
- Role-based access (Admin / Teacher)
- Student Management (MongoDB)
- Course Management (MongoDB)
- Django Admin Panel
- MongoDB for application data
- SQLite for authentication (Django default)
## Tech Stack:
- Backend:Django 6.0  
- API: Django REST Framework  
- Authentication:Simple JWT  
- Database:
- MongoDB → Students & Courses  
- SQLite → Users & Auth  
- ORM:MongoEngine  
- API Client:Thunder Client / Postman
## Project Structure:
```
  student_management/
│
├── core/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── student_management/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── manage.py
└── README.md
```
## Create Virtual Environment :
```
python -m venv venv
venv\Scripts\activate
```
## Install Dependencies :  
```
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install mongoengine
pip install pymongo
```
## Start MongoDB:
```
localhost:27017
```
## Run Migrations(SQLite only):
```
python manage.py migrate
```
## Create Superuser:
```
python manage.py createsuperuser
```
## Run Server:
```
python manage.py runserver
```
