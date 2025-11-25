from django.urls import path
from . import views
from .views import (
    PlaceListAPIView,
    PlaceDetailAPIView,
    PlaceCreateAPIView,
    PhotoListAPIView,
    PhotoDetailAPIView,
    PhotoCreateAPIView,
)

app_name = 'places'

urlpatterns = [
    # Web views
    path('', views.map_view, name='map'),
    path('place/<slug:slug>/', views.place_detail, name='detail'),

    # Simple JSON endpoint for map
    path('api/places-lite/', views.places_api, name='places_api'),

    # Places API
    path('api/places/', PlaceListAPIView.as_view(), name='api-places'),
    path('api/places/add/', PlaceCreateAPIView.as_view(), name='api-place-add'),
    path('api/places/<slug:slug>/', PlaceDetailAPIView.as_view(), name='api-place-detail'),

    # Photos API
    path('api/photos/', PhotoListAPIView.as_view(), name='api-photos'),
    path('api/photos/add/', PhotoCreateAPIView.as_view(), name='api-photo-add'),
    path('api/photos/<int:pk>/', PhotoDetailAPIView.as_view(), name='api-photo-detail'),
]

