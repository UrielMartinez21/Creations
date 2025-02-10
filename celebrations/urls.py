from django.urls import path
from . import views


app_name = 'celebrations'

urlpatterns = [
    path('valentine_v1/', views.valentine_v1, name='valentine_v1'),
    path('yellow_flowers/', views.yellow_flowers, name='yellow_flowers'),
    path('dentist/', views.dentist, name='dentist'),
]