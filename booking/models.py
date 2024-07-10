from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    facilities = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    capacity = models.IntegerField()


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=BOOKING_STATUS_CHOICES,
        default='CONFIRMED')
