from django.urls import path,re_path
from . import views

app_name = 'basketball'

urlpatterns = [
    path('news/', views.NewsModelListAPI.as_view(), name='news'),
    path('recent_class/', views.RecentClassListAPI.as_view(), name='recent_class'),
    re_path('class/(?P<slug>[-\w]+)/', views.ClassByTypeAPIView.as_view(), name='class'),
    path('home_class/', views.HomeClassListAPI.as_view(), name="home_class"),
    path('blog/', views.BlogModelListAPI.as_view(), name='blog'),
    path('recent_image/', views.RecentImageListAPIView.as_view(), name='recent_image'),
    re_path('image/(?P<slug>[-\w]+)/', views.ImageByCategoryAPIView.as_view(), name='image'),
    path('staff/', views.StaffModelListAPI.as_view(), name='staff'),
    path('boss/', views.BossModelListAPI.as_view(), name="boss"),
    path('committee/', views.CommitteeModelListAPI.as_view(), name="committee"),
    path('about/', views.AboutModelListAPI.as_view(), name="about"),
    path('league/', views.LeagueModelListAPI.as_view(), name="league"),
]
