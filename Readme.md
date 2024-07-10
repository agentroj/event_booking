# Event Booking Platform

This repository contains the backend system for an Event Booking Platform, built using Django and Django REST Framework. The platform manages venues, events, user profiles, and bookings.

## Table of Contents
1. [Local Environment Setup](#local-environment-setup)
    - [Dockerized Setup](#dockerized-setup)
    - [Non-Dockerized Setup](#non-dockerized-setup)
2. [Environment Variables](#environment-variables)
3. [Database Migration and Superuser Creation](#database-migration-and-superuser-creation)
4. [API Endpoints and Sample Payloads](#api-endpoints-and-sample-payloads)
5. [Database Schema](#database-schema)
6. [Scalability and Performance](#scalability-and-performance)
7. [Security Considerations](#security-considerations)
8. [Postman Collection](#postman-collection)

## Local Environment Setup

### Dockerized Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/agentroj/event_booking.git
    cd event_booking
    ```

2. **Create a `.env` file in the project root:**
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=event_booking
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

3. **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

4. **Run migrations and create a superuser:**
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

### Non-Dockerized Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/agentroj/event_booking.git
    cd event_booking
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project root:**
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=event_booking
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    ```

5. **Configure PostgreSQL database:**
    - Ensure PostgreSQL is installed and running.
    - Create a database with the name specified in the `.env` file.
    - Create a user with the credentials specified in the `.env` file and grant necessary privileges.

6. **Run migrations and create a superuser:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Environment Variables

Create a `.env` file in the root directory with the following content:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=event_booking
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db  # Use 'localhost' if not using Docker
DB_PORT=5432
```

# Database Migration and Superuser Creation

## Run database migrations:
```
python manage.py migrate
```

## Create a superuser:
```
python manage.py createsuperuser
```

# API Endpoints and Sample Payloads

## User Registration and Authentication

### POST /api/users/
Request:
```
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "password123"
}
```

Response:
```
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com"
}
```

## Venue Management

### POST /api/venues/
Request:
```
{
  "name": "Conference Hall",
  "location": "123 Main St",
  "capacity": 200,
  "facilities": "WiFi, Projector"
}
```

Response:
```
{
  "id": 1,
  "name": "Conference Hall",
  "location": "123 Main St",
  "capacity": 200,
  "facilities": "WiFi, Projector"
}
```


### GET /api/venues/1/

Response:
```
{
  "id": 1,
  "name": "Conference Hall",
  "location": "123 Main St",
  "capacity": 200,
  "facilities": "WiFi, Projector"
}
```

### PUT /api/venues/1/
Request:
```
{
  "name": "Updated Conference Hall",
  "location": "123 Main St",
  "capacity": 250,
  "facilities": "WiFi, Projector, Sound System"
}
```

Response:
```
{
  "id": 1,
  "name": "Updated Conference Hall",
  "location": "123 Main St",
  "capacity": 250,
  "facilities": "WiFi, Projector, Sound System"
}
```
## Event Management

### POST /api/events/
Request:
```
{
  "title": "Tech Conference",
  "description": "A conference about the latest in tech.",
  "date": "2024-08-01",
  "time": "10:00:00",
  "venue": 1,
  "capacity": 200
}
```

Response:
```
{
  "id": 1,
  "title": "Tech Conference",
  "description": "A conference about the latest in tech.",
  "date": "2024-08-01",
  "time": "10:00:00",
  "venue": 1,
  "capacity": 200
}
```

### GET /api/events/1/
Response:
```
{
  "id": 1,
  "title": "Tech Conference",
  "description": "A conference about the latest in tech.",
  "date": "2024-08-01",
  "time": "10:00:00",
  "venue": 1,
  "capacity": 200
}
```

## Booking Management

### POST /api/bookings/
Request:
```
{
  "user": 1,
  "event": 1
}
```

Response:
```
{
  "id": 1,
  "user": 1,
  "event": 1,
  "booking_date": "2024-07-10T12:00:00Z",
  "status": "CONFIRMED"
}
```

### GET /api/bookings/1/

Response:
```
{
  "id": 1,
  "user": 1,
  "event": 1,
  "booking_date": "2024-07-10T12:00:00Z",
  "status": "CONFIRMED"
}
```
### POST /api/bookings/1/cancel/
Request:
```
{}
```

Response:
```
{
  "id": 1,
  "status": "CANCELLED"
}
```

## User Booking History
### GET /api/users/1/booking-history/

Response:
```
[
  {
    "id": 1,
    "user": 1,
    "event": 1,
    "booking_date": "2024-07-10T12:00:00Z",
    "status": "CANCELLED"
  },
  {
    "id": 2,
    "user": 1,
    "event": 2,
    "booking_date": "2024-07-15T12:00:00Z",
    "status": "CONFIRMED"
  }
]
```

# Note:
This README provides a comprehensive guide for setting up the local environment, 
configuring environment variables, running database migrations, creating a superuser, 
and provides sample payloads and responses for the API endpoints.



# Database Schema:
![image](https://github.com/agentroj/event_booking/assets/37651790/6501d983-b509-4734-b52f-a83688e89ef7)


# Scalability and Performance
To ensure the system can handle high volumes of simultaneous users and bookings, consider the following strategies:

## 1. Database Optimization:

Indexes: Create indexes on frequently queried fields to speed up read operations.
Query Optimization: Ensure that database queries are efficient and use joins, where appropriate, instead of multiple separate queries.
### Sample implementation:
    ```
    from django.db.models import Index
    
    class Booking(models.Model):
        ...
        class Meta:
            indexes = [
                Index(fields=['user', 'event']),
            ]
    ```

## 2. Caching:
    Use caching mechanisms (e.g., Redis, Memcached) to store frequently accessed data and reduce the load on the database.

### Sample implementation:
    ```
    from django.core.cache import cache
    
    def get_event(event_id):
        event = cache.get(f'event_{event_id}')
        if not event:
            event = Event.objects.get(id=event_id)
            cache.set(f'event_{event_id}', event)
        return event
    ```
    
## Load Balancing:
    Deploy the application across multiple servers and use a load balancer (e.g., Nginx, AWS ELB) to distribute incoming traffic.

## Horizontal Scaling:
    Add more application servers and database replicas to handle increased load.

## Asynchronous Processing:
### Sample implementation:
    Use task queues (e.g., Celery, RabbitMQ) for handling long-running tasks asynchronously to improve response times.
    ```
    from celery import shared_task
    
    @shared_task
    def send_booking_confirmation_email(booking_id):
        # Logic to send email
        pass
    ```


# Security Considerations
To protect user data and prevent common vulnerabilities, implement the following security measures:

## 1. Input Validation and Sanitization:
    Validate and sanitize all user inputs to prevent SQL injection, cross-site scripting (XSS), and other injection attacks.
### Sample implementation:
    ```
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    
    def validate_user_input(email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("Invalid email format")
    ```
    
## 2. Authentication and Authorization:
   1. **Use Django's built-in authentication system and extend it as needed to handle user registration, login, and permissions.**
   2. **Use JWT or OAuth for secure token-based authentication.**
    
### Sample implementation:
   ```
    from rest_framework_simplejwt.tokens import RefreshToken
    
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
   ```

## 3. Authentication and Authorization:
Use HTTPS to encrypt data in transit between the client and server.


## 4. CSRF Protection:
Enable Cross-Site Request Forgery (CSRF) protection for all forms and POST requests.
### Sample implementation:
```
from django.middleware.csrf import CsrfViewMiddleware
```

## 5. Error Handling:
Implement proper error handling to avoid exposing sensitive information in error messages.
### Sample implementation:

```
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response
```

## 5.Data Encryption:
Encrypt sensitive data (e.g., passwords) at rest using secure hashing algorithms like bcrypt.
### Sample implementation:

```
from django.contrib.auth.hashers import make_password

def create_user(username, email, password):
    hashed_password = make_password(password)
    User.objects.create(username=username, email=email, password=hashed_password)
```



# Postman Collection
You can find the Postman collection to test the API endpoints in the repository. Import the postman_collection.json file into Postman to get started.

[Uploading postman_collection.json…]()






