# Inventory Management System API

## Overview

This project implements a **Backend API** for an **Inventory Management System** using **Django Rest Framework (DRF)**. The system supports **CRUD operations** for inventory items, secured with **JWT authentication**. The API interacts with a **PostgreSQL database**, uses **Redis for caching** frequently accessed items, and integrates a **logging system** for monitoring and debugging. Unit tests ensure the functionality of all endpoints.

## Features

- **JWT Authentication**: Secure all endpoints (register, login, CRUD operations).
- **CRUD Endpoints**: Create, Read, Update, Delete inventory items.
- **Caching with Redis**: Frequently accessed items are cached for improved performance.
- **Logging**: Track API usage and errors with detailed logs.
- **Unit Tests**: Comprehensive tests to ensure correct functionality.

## Requirements

- **Python 3.x**
- **Django** 3.0+
- **Django Rest Framework**
- **PostgreSQL** (for database)
- **Redis** (for caching)
- **pytest** (for running unit tests)

## Setup Instructions

1. **Clone the repository**:
   git clone <repository_url>
   cd <repository_name>

2. **Install dependencies**:
   pip install -r requirements.txt

3. **Set up the database**:
   - Install and configure PostgreSQL.
   - Create a database for the project.
   - Apply database migrations:
     python manage.py migrate

4. **Set up Redis** (Ensure Redis is installed and running):
   - If Redis is not running, you can start it with:
     redis-server

5. **Configure environment variables**:
   - Set the following environment variables:
     - `DATABASE_URL` (PostgreSQL connection string)
     - `SECRET_KEY` (for JWT tokens)
     - `REDIS_URL` (Redis connection URL)

6. **Run the development server**:
   python manage.py runserver

7. **Access the API**:
   - The API will be available at `http://127.0.0.1:8000/`.
   - All CRUD operations are secured using JWT. First, authenticate by registering and logging in to get a token.

## API Endpoints

- **POST /items/**: Create a new inventory item.
- **GET /items/{item_id}/**: Get details of an inventory item.
- **PUT /items/{item_id}/**: Update an existing inventory item.
- **DELETE /items/{item_id}/**: Delete an inventory item.

## Testing

To run unit tests, use:
python manage.py test

## Logging

All API usage, errors, and other significant events are logged to the console and can be configured in `settings.py`.

## Notes

- Make sure to have Redis and PostgreSQL running before starting the server.
- JWT authentication is required for all endpoints except for registration and login.
