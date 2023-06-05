from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ShopperSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
         model = UserModel
         fields = ["id", "username", "email", "password", "phone_number"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=15, write_only=True)

class PasswordResetSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])

# serializers.py

# from rest_framework import serializers
# from .models import Shopper


# class ShopperSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shopper
#         fields = ["id", "username", "email", "phone_number"]

    