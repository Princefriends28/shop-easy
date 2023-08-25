from django.urls import path, include
from rest_framework import routers

from .viewsets import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', ProfileViewSet.as_view(), name='profile'),
]
