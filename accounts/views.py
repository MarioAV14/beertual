from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyUser(APIView):
    def get(self, request, format=None):
        my_user = Profile.objects.all().get(usuario=request.user.id)
        serializer = ProfileSerializer(my_user)
        return Response(serializer.data)