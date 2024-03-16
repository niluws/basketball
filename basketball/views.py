from rest_framework import generics

from .models import NewsModel, ClassModel, ImageCategoryModel, StaffModel, BlogModel, LeagueTableModel, LeagueModel, \
    AboutModel, BossModel, CommitteeModel, ClassDetailModel
from .serializers import NewsModelSerializer, ClassModelSerializer, ImageCategoryModelSerializer, StaffModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, LeagueModelSerializer, LeagueTableSerializer, BossModelSerializer, \
    CommitteeModelSerializer, ClassDetailModelSerializer


class NewsModelListAPI(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class ClassModelListAPI(generics.ListAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassModelSerializer


class HomeClassListAPI(generics.ListAPIView):
    queryset = ClassDetailModel.objects.filter(show=True)
    serializer_class = ClassDetailModelSerializer


class BlogModelListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = ImageCategoryModel.objects.all()
    serializer_class = ImageCategoryModelSerializer


# todo Committee shows by genders{roll{gender{name and image--mabe change the table
class StaffModelListAPI(generics.ListAPIView):
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializer


class BossModelListAPI(generics.ListAPIView):
    queryset = BossModel.objects.all().order_by('full_name')
    serializer_class = BossModelSerializer


class CommitteeModelListAPI(generics.ListAPIView):
    queryset = CommitteeModel.objects.all().order_by('full_name')
    serializer_class = CommitteeModelSerializer


class AboutModelListAPI(generics.ListAPIView):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer

    # todo get just the last about


class LeagueModelListAPI(generics.ListAPIView):
    queryset = LeagueModel.objects.all()
    serializer_class = LeagueModelSerializer


class LeagueTableListAPI(generics.ListAPIView):
    queryset = LeagueTableModel.objects.all()
    serializer_class = LeagueTableSerializer
