from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Venue, Event, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'status']
