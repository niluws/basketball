from rest_framework import generics
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"error": "No data found"}, status=404)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LeagueModelListAPI(generics.ListAPIView):
    queryset = LeagueModel.objects.all()
    serializer_class = LeagueModelSerializer


class LeagueTableListAPI(generics.ListAPIView):
    queryset = LeagueTableModel.objects.all()
    serializer_class = LeagueTableSerializer
