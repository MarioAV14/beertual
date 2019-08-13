from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import OfertasSerializer
from .serializers import ImagenesSerializer
from .serializers import BaresSerializer
from .serializers import BebidasSerializer
from .models import Bebidas
from .models import Bares
from .models import Imagenes
from .models import Ofertas

# Create your views here.

class OfertasViewSet(viewsets.ModelViewSet):
    queryset=Ofertas.objects.all()
    serializer_class=OfertasSerializer

class ImagenesViewSet(viewsets.ModelViewSet):
    queryset=Imagenes.objects.all()
    serializer_class=ImagenesSerializer

class BaresViewSet(viewsets.ModelViewSet):
    queryset=Bares.objects.all()
    serializer_class=BaresSerializer

class BebidasViewSet(viewsets.ModelViewSet):
    queryset=Bebidas.objects.all()
    serializer_class=BebidasSerializer