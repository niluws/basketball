from rest_framework import viewsets, permissions

from .models import NewsModel, ClassModel, ImagesModel, StaffMemberModel, BlogModel, LeagueTableModel, LeagueModel, \
    AboutModel
from .serializers import NewsModelSerializer, ClassModelSerializer, ImageModelSerializer, StaffMemberModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, LeagueModelSerializer, LeagueTableSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class ClassModelViewSet(viewsets.ModelViewSet):
    queryset = ClassModel.objects.all()
    serializer_class = ClassModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class BlogModelViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImageModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class MemberModelViewSet(viewsets.ModelViewSet):
    queryset = StaffMemberModel.objects.all()
    serializer_class = StaffMemberModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class AboutModelViewSet(viewsets.ModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class LeagueModelViewSet(viewsets.ModelViewSet):
    queryset = LeagueModel.objects.all()
    serializer_class = LeagueModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class LeagueTableViewSet(viewsets.ModelViewSet):
    queryset = LeagueTableModel.objects.all()
    serializer_class = LeagueTableSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
