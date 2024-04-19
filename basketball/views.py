from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.response import Response

from .models import NewsModel, ClassModel, ImageCategoryModel, StaffModel, BlogModel, LeagueModel, \
    AboutModel, BossModel, ClassDetailModel, RoleModel, CommitteeModel
from .serializers import NewsModelSerializer, RecentImageCategoryModelSerializer, \
    StaffModelSerializer, \
    BlogModelSerializer, AboutModelSerializer, LeagueModelSerializer, BossModelSerializer, \
    ClassDetailModelSerializer, RoleModelSerializer, ImageCategoryModelSerializer, ClassSerializer, BannerSerializer


class NewsListAPI(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class NewsDetailListAPI(generics.RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer
    lookup_field = 'id'


class BannerAPI(generics.ListAPIView):
    queryset = NewsModel.objects.all()[:3]
    serializer_class = BannerSerializer


class HomeClassListAPI(generics.ListAPIView):
    """
    این کلاس ها در صفحه ای که تمام دورها را نمایش میدهد استفاده میشود
    """
    queryset = ClassDetailModel.objects.filter(show=True)
    serializer_class = ClassDetailModelSerializer


class ClassListAPI(generics.ListAPIView):
    """
    این کلاس ها در صفحه ای که تمام دوره ها را نمایش میدهد استفاده میشود
    """
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializer


class ClassDetailAPIView(generics.ListAPIView):
    """
     جزیئات کلاس
    """
    serializer_class = ClassDetailModelSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = ClassDetailModel.objects.filter(slug=slug)
        return queryset


class BlogModelListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer


class RecentImageListAPIView(generics.ListAPIView):
    """
    دسته بندی ها و 4 عکس اخیر از هر دسته بندی را نمایش میدهد
    """
    queryset = ImageCategoryModel.objects.prefetch_related('image')
    serializer_class = RecentImageCategoryModelSerializer


class ImageByCategoryAPIView(generics.ListAPIView):
    """
    تمام عکسای مربوط به یک دسته بندی را نمایش میدهد
    """
    serializer_class = ImageCategoryModelSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            category = ImageCategoryModel.objects.get(slug=slug)
            return [category]
        except ImageCategoryModel.DoesNotExist:
            return ImageCategoryModel.objects.none()

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
    queryset = RoleModel.objects.prefetch_related(
        Prefetch('role', queryset=CommitteeModel.objects.order_by('full_name'))
    )
    serializer_class = RoleModelSerializer


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
    serializer_class = LeagueModelSerializer

    def get_queryset(self):
        return LeagueModel.objects.filter(available=True).prefetch_related(
            'leaguegroupmodel_set',
            'leaguegroupmodel_set__leaguetablemodel_set',
        )
