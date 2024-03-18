from rest_framework import serializers
from authentication.models import User


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
