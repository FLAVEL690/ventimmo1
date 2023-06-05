from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from .serializers import ShopperSerializer, LoginSerializer, PasswordResetSerializer

UserModel = get_user_model()

class ShopperCreateAPIView(CreateAPIView):
    serializer_class = ShopperSerializer
    permission_classes = (AllowAny,)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({'username': ['Invalid username or password.']}, status=status.HTTP_400_BAD_REQUEST)
        response_data = {
            'id': user.id,
            'phone_number': user.phone_number,
            'email': user.email,
            'username': user.username
        }
        return Response(response_data)


class PasswordResetAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        email = serializer.validated_data['email']
        user_queryset = UserModel.objects.filter(phone_number=phone_number, email=email)
        if not user_queryset.exists():
            return Response({'detail': 'Invalid phone number or email.'}, status=status.HTTP_400_BAD_REQUEST)

        user = user_queryset.first()
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')
        token = default_token_generator.make_token(user)
        reset_url = f"{request.get_host()}/api/auth/password_reset_confirm/{uid}/{token}"
        message = f"Hello {user.username},\n\nPlease reset your password by clicking on the link: {reset_url}\n\nBest regards,\nThe KapyGenius Team"

        send_mail(
            subject="Reset your password",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )

        return Response({'detail': f'Password reset link has been sent to {email}.'}, status=status.HTTP_204_NO_CONTENT)


class PasswordResetConfirmAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password = serializer.validated_data['password']
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Your password has been reset.'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # views.py

from rest_framework import status
from rest_framework import generics
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Shopper
from .serializers import ShopperSerializer
from django.shortcuts import get_object_or_404



class DeleteShopperView(DestroyAPIView):
    queryset = Shopper.objects.all()
    serializer_class = ShopperSerializer
    permission_classes = [IsAdminUser]
    
    

class ListShopperView(ListAPIView):
    queryset= Shopper.objects.all()
    serializer_class= ShopperSerializer
    