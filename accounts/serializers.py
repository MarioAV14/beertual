from  django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from directorio.serializers import BaresSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['num_telefono','foto','slug']

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    profile_usuario=ProfileSerializer()
    user_bar=BaresSerializer()
    class Meta:
        model= User
        fields=['username', 'first_name', 'last_name', 'email', 'password', 'id', 'profile_usuario','user_bar']

    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return  user