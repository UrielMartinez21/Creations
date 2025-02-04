from django.urls import path
from . import views


app_name = 'flowers'

urlpatterns = [
    path('yellow_flowers/', views.yellow_flowers, name='yellow_flowers'),
]