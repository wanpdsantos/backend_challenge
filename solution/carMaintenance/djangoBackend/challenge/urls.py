from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cars', views.CarEventsViewset, basename='car')

urlpatterns = [
  path('api/', include(router.urls))
]