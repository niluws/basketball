from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'password', 'confirm_password','roll']

    def validate(self, attrs):
        attrs.pop('confirm_password')
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']


class LogoutSerializer(serializers.Serializer):
    pass

# class VerifyEmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']
#
