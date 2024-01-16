from rest_framework import viewsets

from .models import NewsModel, NoticeModel, ImagesModel
from .serializers import NewsModelSerializer, NoticeModelSerializer, ImagesModelSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class NoticeModelViewSet(viewsets.ModelViewSet):
    queryset = NoticeModel.objects.all()
    serializer_class = NoticeModelSerializer


class ImagesModelViewSet(viewsets.ModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesModelSerializer
