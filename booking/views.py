# booking/views.py
from rest_framework import viewsets, status # noqa
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Venue, Event, Booking
from .serializers import (UserSerializer, VenueSerializer, EventSerializer,
                          BookingSerializer, BookingCancelSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def booking_history(self, request, pk=None):
        user = self.get_object()
        bookings = Booking.objects.filter(user=user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'CANCELLED'
        booking.save()
        serializer = BookingCancelSerializer(booking)
        return Response(serializer.data)
