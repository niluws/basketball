from rest_framework.routers import DefaultRouter

from .views import NewsModelViewSet, ClassModelViewSet, ImageModelViewSet, MemberModelViewSet, BlogModelViewSet, \
    AboutModelViewSet, LeagueModelViewSet, LeagueTableViewSet

app_name = 'basketball'
router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'class', ClassModelViewSet, basename='class')
router.register(r'blog', BlogModelViewSet, basename='blog')
router.register(r'image', ImageModelViewSet, basename='image')
router.register(r'member', MemberModelViewSet, basename='member')
router.register(r'about', AboutModelViewSet, basename='about')
router.register(r'league', LeagueModelViewSet, basename='league')
router.register(r'league_table', LeagueTableViewSet, basename='league_table')

urlpatterns = router.urls
