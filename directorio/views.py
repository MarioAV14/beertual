from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.

class OfertasViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=OfertasSerializer
    def get_queryset(self, *args, **kwargs):
        oferta=self.request.GET.get('idbar')
        queryset_list=super(OfertasViewSet, self).get_queryset()
        if oferta:
            queryset_list=queryset_list.filter(nombre_bar__id=oferta)
        return queryset_list

class ImagenesViewSet(viewsets.ModelViewSet):
    queryset=Imagenes.objects.all()
    serializer_class=ImagenesSerializer
    def get_queryset(self, *args, **kwargs):
        imagen=self.request.GET.get('idbar')
        queryset_list=super(ImagenesViewSet, self).get_queryset()
        if imagen:
            queryset_list=queryset_list.filter(nombre_bar__id=imagen)
        return queryset_list

class BaresViewSet(viewsets.ModelViewSet):
    queryset=Bar.objects.all()
    serializer_class=BaresSerializer
    def get_queryset(self, *args, **kwargs):
        slug=self.request.GET.get('slug')
        user=self.request.GET.get('iduser')
        queryset_list=super(BaresViewSet, self).get_queryset()
        if slug:
            queryset_list=queryset_list.filter(slug=slug)
        if user:
            queryset_list=queryset_list.filter(usuario__id=user)
        return queryset_list

class BebidasViewSet(viewsets.ModelViewSet):
    queryset=Bebidas.objects.all()
    serializer_class=BebidasSerializer
    def get_queryset(self, *args, **kwargs):
        bebida=self.request.GET.get('idbar')
        queryset_list=super(BebidasViewSet, self).get_queryset()
        if bebida:
            queryset_list=queryset_list.filter(nombre_bar__id=bebida)
        return queryset_list

class GETOfertasViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=GETOfertasSerializer
