from rest_framework import serializers

from .models import SettingsModel


class SettingsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = '__all__'
