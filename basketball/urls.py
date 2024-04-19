from django.urls import path,re_path
from . import views

app_name = 'basketball'

urlpatterns = [
    path('news/', views.NewsListAPI.as_view(), name='news'),
    path('news_detail/<int:id>', views.NewsDetailListAPI.as_view(), name='news_detail'),
    path('banner/', views.BannerAPI.as_view(), name='banner'),
    path('class/', views.ClassListAPI.as_view(), name='recent_class'),
    re_path('class/(?P<slug>[-\w]+)/', views.ClassDetailAPIView.as_view(), name='class'),
    path('class_home/', views.HomeClassListAPI.as_view(), name="class_home"),
    path('blog/', views.BlogModelListAPI.as_view(), name='blog'),
    path('gallery_categories/', views.RecentImageListAPIView.as_view(), name='gallery_categories'),
    re_path('gallery/(?P<slug>[-\w]+)/', views.ImageByCategoryAPIView.as_view(), name='image'),
    path('staff/', views.StaffModelListAPI.as_view(), name='staff'),
    path('boss/', views.BossModelListAPI.as_view(), name="boss"),
    path('committee/', views.CommitteeModelListAPI.as_view(), name="committee"),
    path('about/', views.AboutModelListAPI.as_view(), name="about"),
    path('league/', views.LeagueModelListAPI.as_view(), name="league"),
]
