from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import RegisterFormModel
from .serializers import MeSerializer, RegisterFormSerializer


class MeAPIView(generics.RetrieveUpdateAPIView):
    """
        token format in header
        Bearer <token>
    """
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user


class RegisterFormAPIView(generics.CreateAPIView):
    queryset = RegisterFormModel.objects.all()
    serializer_class = RegisterFormSerializer
