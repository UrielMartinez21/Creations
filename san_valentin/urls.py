from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.main_index, name='main_index'),
    path('index_v1/', views.index_v1, name='index_v1'),
]