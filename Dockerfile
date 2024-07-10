# Dockerfile

FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Run Flake8 and Pytest
RUN flake8
RUN pytest --disable-warnings

# Start server
CMD ["gunicorn", "event_booking.wsgi:application", "--bind", "0.0.0.0:8000"]
