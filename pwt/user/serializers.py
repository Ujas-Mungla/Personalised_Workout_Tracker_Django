from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, OTP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
        
    def create(self, validated_data):
        # Hash the password before saving the user
        user = User(**validated_data)
        user.password = make_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        # Hash the password if it's being updated
        if 'password' in validated_data:
            instance.password = make_password(validated_data.get('password'))
        return super(UserSerializer, self).update(instance, validated_data)

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'

class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
