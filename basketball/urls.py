from rest_framework.routers import DefaultRouter

from .views import NewsModelViewSet, NoticeModelViewSet, ImagesModelViewSet, MemberModelViewSet

app_name = 'basketball'
router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'notices', NoticeModelViewSet, basename='notices')
router.register(r'images', ImagesModelViewSet, basename='images')
router.register(r'members', MemberModelViewSet, basename='members')

urlpatterns = router.urls
