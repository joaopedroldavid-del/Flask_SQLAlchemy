# Flask SQLAlchemy API

A simple RESTful API built with Flask and SQLAlchemy. This project is designed as a sample API for my personal portfolio, demonstrating CRUD operations, database integration, and best practices for developing a Python backend.

## 🚀 Features

- RESTful API with Flask  
- SQLAlchemy ORM for database interactions  
- CRUD operations for managing resources  
- Environment-based configuration  
- Data validation and serialization  
- User authentication with hashed passwords  
- Role-based access control for admin users  
- Secure API with token-based authentication  
- Docker support for easy deployment  

## 🔒 Security & Authentication

### Cryptography  
- User passwords are securely stored using **bcrypt** hashing.  

### Login Required  
- User authentication is required for accessing protected resources.  
- Users must log in with their credentials to receive an **access token**.  
- The token must be included in the **Authorization** header for secured API requests.  

### Admin Users & Role Management  
- The API supports role-based access control (RBAC).  
- Admin users can **create, update, and delete** other user accounts.  
- Regular users have limited permissions and cannot modify admin data.  

## 📖 API Endpoints  

| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| GET    | /items          | Get all items |
| GET    | /items/<id>     | Get item by ID |
| POST   | /items          | Create new item |
| PUT    | /items/<id>     | Update an item |
| DELETE | /items/<id>     | Delete an item |
| POST   | /register       | Register a new user |
| POST   | /login          | Authenticate user and get a token |
| GET    | /admin/users    | Get all users (Admin only) |
| PUT    | /admin/users/<id> | Update user role (Admin only) |
| DELETE | /admin/users/<id> | Delete a user (Admin only) |
