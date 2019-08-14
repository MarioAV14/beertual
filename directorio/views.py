from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.

class OfertasViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=OfertasSerializer

class ImagenesViewSet(viewsets.ModelViewSet):
    queryset=Imagenes.objects.all()
    serializer_class=ImagenesSerializer

class BaresViewSet(viewsets.ModelViewSet):
    queryset=Bar.objects.all()
    serializer_class=BaresSerializer
    def get_queryset(self, *args, **kwargs):
        slug=self.request.GET.get('slug')
        queryset_list=super(BaresViewSet, self).get_queryset()
        if slug:
            queryset_list=queryset_list.filter(slug=slug)
        return queryset_list

class BebidasViewSet(viewsets.ModelViewSet):
    queryset=Bebidas.objects.all()
    serializer_class=BebidasSerializer

class GETOfertasViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=GETOfertasSerializer
