from django.urls import path
from . import views

urlpatterns = [
  path('car', views.Car_View, name='Car'), 
]