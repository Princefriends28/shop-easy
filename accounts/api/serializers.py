from phonenumber_field import serializerfields
from rest_framework import serializers

from ..models import *


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializerfields.PhoneNumberField()
    email = serializers.EmailField()
    is_verified_mail = serializers.BooleanField()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'phone_number', 'email', 'is_verified_mail')


class AuthTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=6)

    class Meta:
        model = AuthToken
        fields = ('id', 'user', 'token', 'created_at')
