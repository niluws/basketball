from rest_framework import generics

from .models import SettingsModel
from .serializers import SettingsModelSerializer


class SettingsAPIView(generics.ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsModelSerializer
