from django.urls import path
from . import views

urlpatterns = [
  path('car', views.Car_View, name='Car'), 
  path('tyre', views.Tyre_View, name='Tyre'), 
]