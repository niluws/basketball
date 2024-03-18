from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (

#     ActiveAccountAPIView,
    LoginAPIView,
    LogoutAPIView,
    RegisterAPIView
#     VerifyEmailAPIView,
#     LogAPIView,
)

app_name = 'authentication'

urlpatterns = [
#     path('activate/<str:otp_code>/', ActiveAccountAPIView.as_view(), name='otp_code'),
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterAPIView.as_view(), name='register')
#     path('verify_email/', VerifyEmailAPIView.as_view(), name='verify_email'),
]
