from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('', views.map_view, name='map'),
    path('api/places/', views.places_api, name='places_api'),
    path('place/<slug:slug>/', views.place_detail, name='detail'),
]
