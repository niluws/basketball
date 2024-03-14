from rest_framework import viewsets

from .models import NewsModel, ClassModel, ImagesModel, StaffModel, BlogModel, LeagueTableModel, LeagueModel, \
    AboutModel, BossModel, CommitteeModel
from .serializers import NewsModelSerializer, ClassModelSerializer, ImageModelSerializer, StaffModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, LeagueModelSerializer, LeagueTableSerializer, BossModelSerializer, \
    CommitteeModelSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer
    http_method_names = ['get']


class ClassModelViewSet(viewsets.ModelViewSet):
    queryset = ClassModel.objects.all()
    serializer_class = ClassModelSerializer
    http_method_names = ['get']



class BlogModelViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    http_method_names = ['get']


class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImageModelSerializer
    http_method_names = ['get']


# todo all members order by alphabet
# todo Committee shows by genders{roll{gender{name and image--mabe change the table
class StaffModelViewSet(viewsets.ModelViewSet):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializer
    http_method_names = ['get']


class BossModelViewSet(viewsets.ModelViewSet):
    queryset = BossModel.objects.all()
    serializer_class = BossModelSerializer
    http_method_names = ['get']


class CommitteeModelViewSet(viewsets.ModelViewSet):
    queryset = CommitteeModel.objects.all()
    serializer_class = CommitteeModelSerializer
    http_method_names = ['get']


class AboutModelViewSet(viewsets.ModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer
    http_method_names = ['get']

    # todo get just the last about


class LeagueModelViewSet(viewsets.ModelViewSet):
    queryset = LeagueModel.objects.all()
    serializer_class = LeagueModelSerializer
    http_method_names = ['get']


class LeagueTableViewSet(viewsets.ModelViewSet):
    queryset = LeagueTableModel.objects.all()
    serializer_class = LeagueTableSerializer
    http_method_names = ['get']
