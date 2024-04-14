import uuid

import redis
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from utils import config, handler
from .models import User
from .serializers import MyTokenObtainPairSerializer
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer

exception_handler = handler.exception_handler
log_user_activity = handler.log_user_activity


@exception_handler
def generate_and_send_otp(email, current_site):
    otp = str(uuid.uuid4())
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set(email, otp, ex=500)

    email_subject = 'Activate Account'
    email_message = f'Click the following link to activate your account:\n' \
                    f' http://{current_site.domain}/auth/activate/{otp}'
    recipient_email = email

    EmailMessage(email_subject, email_message, config.EMAIL_HOST_USER, [recipient_email]).send()


class RegisterAPIView(generics.CreateAPIView):
    """
    roll have 4 types v,s,m,d
    short form of ورزشکار , سرپرست , مربی و داور
    """
    serializer_class = RegisterSerializer

    @exception_handler
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            phone_number = request.data.get('phone_number')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')
            user = User.objects.filter(phone_number=phone_number).first()

            if user:
                return Response({'success': False, 'status': 400,
                                 'error': 'Phone number already exists'})
            elif password != confirm_password:
                return Response({'success': False, 'status': 400, 'error': 'Password fields are not match'})
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            message = {
                'message': 'You registered successfully',
                'first_name': serializer.validated_data.get('first_name'),
                'last_name': serializer.validated_data.get('last_name'),
                'phone_number': phone_number,
                'role': serializer.validated_data.get('role'),
            }
            log = {
                'event': 'Registered',
                'user_id': user.pk,
            }
            return Response({'success': True, 'status': 201, 'message': message, 'log': log})
        except Exception as e:
            return Response({'success': False, 'status': 400, 'error': str(e)})


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    @exception_handler
    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        user = User.objects.filter(phone_number=phone_number).first()

        if not phone_number or not password:
            return Response({'success': False, 'status': 400, 'error': 'Phone number and password are required'})

        if user:
            if user.is_active:
                if not user.check_password(password):
                    return Response({'success': False, 'status': 401, 'error': 'Incorrect password'})
                user = authenticate(phone_number=phone_number, password=password)
                refresh = RefreshToken.for_user(user)
                # generate_and_send_otp(phone_number)
                message = {
                    'message': 'You logged in successfully',
                    'data': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    },
                }
                log = {
                    'event': 'Logged in',
                    'user_id': user.pk,
                }
                return Response({'success': True, 'status': 200, 'message': message, 'log': log})
            else:
                return Response({'success': False, 'status': 401, 'error': 'Verify your account'})
        else:
            return Response({'success': False, 'status': 401, 'error': 'Phone number not found.'})


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    @exception_handler
    def post(self, request):
        if request.user.is_authenticated:
            message = {
                'message': 'You Logout successfully',
            }
            log = {
                'event': 'Logout',
                'user_id': request.user.pk,
            }
            return Response({'success': True, 'status': 200, 'message': message, 'log': log})
        else:
            return Response({'success': False, 'status': 401, 'error': 'User is not authenticated'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'success': False, 'error': 'Token is invalid or expired'}, status=400)

        return Response(serializer.validated_data, status=200)

# class ActiveAccountAPIView(views.APIView):
#
#     @exception_handler
#     def get(self, request, otp_code):
#
#         r = redis.Redis(host='localhost', port=6379, db=0)
#         keys = r.keys('*')
#
#         for key in keys:
#
#             value = r.get(key)
#
#             if value.decode('utf-8') == otp_code:
#                 user = User.objects.filter(email=key.decode('utf-8')).first()
#                 user.is_active = True
#                 user.save()
#                 r.delete(key)
#
#                 return Response({'success': True, 'status': 200, 'message': 'Account activated successfully'})
#
#         return Response({'success': False, 'status': 404, 'error': 'Invalid OTP code'})

