from rest_framework import generics

from accounts.models import Profile, AuthToken
from .serializers import *


class ProfileViewSet(generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # def post(self, request, *args, **kwargs):


class AuthTokenViewSet(generics.GenericAPIView):
    queryset = AuthToken.objects.all()
    serializer_class = AuthTokenSerializer
