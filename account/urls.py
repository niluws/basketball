from django.urls import path

from .views import MeAPIView

app_name = 'profile'

urlpatterns = [
    path('me/', MeAPIView.as_view(), name='me'),

]
