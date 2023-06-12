from rest_framework import routers

from django.urls import path, include
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'auth-token', AuthTokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/', ProfileViewSet.as_view(), name='profile'),
]

