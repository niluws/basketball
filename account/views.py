from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import MeSerializer


class MeAPIView(generics.RetrieveUpdateAPIView):
    """
        token format in header
        Bearer <token>
    """
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
