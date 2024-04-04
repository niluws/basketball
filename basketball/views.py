from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.response import Response

from .models import NewsModel, ClassModel, ImageCategoryModel, StaffModel, BlogModel, LeagueModel, \
    AboutModel, BossModel, ClassDetailModel, RollModel, CommitteeModel, ImagesModel
from .serializers import NewsModelSerializer, RecentImageCategoryModelSerializer, \
    StaffModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, LeagueModelSerializer, BossModelSerializer, \
    ClassDetailModelSerializer, RollModelSerializer, ImageModelSerializer, RecentClassSerializer


class NewsModelListAPI(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class HomeClassListAPI(generics.ListAPIView):
    queryset = ClassDetailModel.objects.filter(show=True)
    serializer_class = ClassDetailModelSerializer


class RecentClassListAPI(generics.ListAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = RecentClassSerializer


class ClassByTypeAPIView(generics.ListAPIView):
    serializer_class = ClassDetailModelSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = ClassDetailModel.objects.filter(class_type__slug__exact=slug)
        return queryset


class BlogModelListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class RecentImageListAPIView(generics.ListAPIView):
    queryset = ImageCategoryModel.objects.prefetch_related('image')
    serializer_class = RecentImageCategoryModelSerializer


class ImageByCategoryAPIView(generics.ListAPIView):
    serializer_class = ImageModelSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            category = ImageCategoryModel.objects.get(slug=slug)
            images = category.image.all()
            return images
        except ImageCategoryModel.DoesNotExist:
            return ImagesModel.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StaffModelListAPI(generics.ListAPIView):
    """
    اعضای هیئت(اصلی)
    """
    queryset = StaffModel.objects.all()
    serializer_class = StaffModelSerializer


class BossModelListAPI(generics.ListAPIView):
    """
    روسای شهرستان
    """
    queryset = BossModel.objects.all().order_by('full_name')
    serializer_class = BossModelSerializer


class CommitteeModelListAPI(generics.ListAPIView):
    """
    اعضای کمیته
    """
    queryset = RollModel.objects.prefetch_related(
        Prefetch('roll', queryset=CommitteeModel.objects.order_by('full_name'))
    )
    serializer_class = RollModelSerializer


class AboutModelListAPI(generics.ListAPIView):
    """
        در این بخش از ckeditor استفاده شده است
    """
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"error": "No data found"}, status=404)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LeagueModelListAPI(generics.ListAPIView):
    queryset = LeagueModel.objects.filter(available=True)
    serializer_class = LeagueModelSerializer
