import pytest
from django.urls import reverse
import os
import django
from django.conf import settings # noqa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_booking.settings')
django.setup()
from rest_framework import status # noqa
from rest_framework.test import APIClient # noqa


@pytest.mark.django_db
def test_api_endpoints():
    client = APIClient()

    # Test User Registration endpoint
    url = reverse('user-list')
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201

    # Test Venue Management endpoint
    url = reverse('venue-list')
    data = {
        'name': 'Test Venue',
        'location': '123 Test St',
        'capacity': 100,
        'facilities': 'WiFi'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

    # Add more endpoint tests as needed
