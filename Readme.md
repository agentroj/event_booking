# Event Booking Platform

This repository contains the backend system for an Event Booking Platform, built using Django and Django REST Framework. The platform manages venues, events, user profiles, and bookings.

## Table of Contents
1. [Local Environment Setup](#local-environment-setup)
    - [Dockerized Setup](#dockerized-setup)
    - [Non-Dockerized Setup](#non-dockerized-setup)
2. [Environment Variables](#environment-variables)
3. [Database Migration and Superuser Creation](#database-migration-and-superuser-creation)
4. [API Endpoints and Sample Payloads](#api-endpoints-and-sample-payloads)

## Local Environment Setup

### Dockerized Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/event-booking-platform.git
    cd event-booking-platform
    ```

2. **Create a `.env` file in the project root:**
    ```env
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=event_booking
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=db
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
    git clone https://github.com/yourusername/event-booking-platform.git
    cd event-booking-platform
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





