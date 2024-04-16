from django.urls import path

from .views import MeAPIView, RegisterFormAPIView

app_name = 'profile'

urlpatterns = [
    path('me/', MeAPIView.as_view(), name='me'),
    path('register_form/', RegisterFormAPIView.as_view(), name='register_form'),

]
