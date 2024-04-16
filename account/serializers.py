from rest_framework import serializers

from authentication.models import User
from .models import RegisterFormModel


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class RegisterFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterFormModel
        fields = "__all__"
