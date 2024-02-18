from rest_framework import viewsets, permissions

from .models import NewsModel, NoticeModel, ImagesModel, MemberModel
from .serializers import NewsModelSerializer, NoticeModelSerializer, ImagesModelSerializer, MemberModelSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class NoticeModelViewSet(viewsets.ModelViewSet):
    queryset = NoticeModel.objects.all()
    serializer_class = NoticeModelSerializer


class ImagesModelViewSet(viewsets.ModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesModelSerializer


class MemberModelViewSet(viewsets.ModelViewSet):
    queryset = MemberModel.objects.all()
    serializer_class = MemberModelSerializer
