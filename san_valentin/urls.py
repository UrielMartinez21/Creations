from django.urls import path
from . import views


app_name = 'san_valentin'

urlpatterns = [
    path('index_v1/', views.index_v1, name='index_v1'),
]