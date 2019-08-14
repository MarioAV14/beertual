from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import EmpresaSerializer
from .models import Empresa

# Create your views here.

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer
