from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, VenueViewSet, EventViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'users/<int:pk>/booking-history/',
        UserViewSet.as_view({'get': 'booking_history'}),
        name='user-booking-history'),
    path(
        'bookings/<int:pk>/cancel/',
        BookingViewSet.as_view({'post': 'cancel'}),
        name='booking-cancel'),
]
