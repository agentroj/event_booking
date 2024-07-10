import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import dotenv
dotenv.load_dotenv()


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
