import pytest
from django.contrib.auth.models import User
from booking.models import Venue, Event, Booking
import dotenv

dotenv.load_dotenv()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='testuser', password='testpass')
    assert user.username == 'testuser'


@pytest.mark.django_db
def test_create_venue():
    venue = Venue.objects.create(
        name='Test Venue',
        location='123 Test St',
        capacity=100,
        facilities='Test Facilities')
    assert venue.name == 'Test Venue'


@pytest.mark.django_db
def test_create_event():
    venue = Venue.objects.create(
        name='Test Venue',
        location='123 Test St',
        capacity=100,
        facilities='Test Facilities')
    event = Event.objects.create(
        title='Test Event',
        description='Test Description',
        date='2024-08-01',
        time='10:00:00',
        venue=venue, capacity=100)
    assert event.title == 'Test Event'


@pytest.mark.django_db
def test_create_booking():
    user = User.objects.create_user(username='testuser', password='testpass')
    venue = Venue.objects.create(
        name='Test Venue',
        location='123 Test St',
        capacity=100,
        facilities='Test Facilities')
    event = Event.objects.create(
        title='Test Event',
        description='Test Description',
        date='2024-08-01',
        time='10:00:00',
        venue=venue,
        capacity=100)
    booking = Booking.objects.create(user=user, event=event)
    assert booking.user == user
