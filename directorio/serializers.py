from rest_framework import serializers
from .models import Bares
from .models import Bebidas
from .models import Imagenes
from .models import Ofertas

class BaresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bares
        fields=['id','titulo_bar', 'logo_bar', 'descripcion_bar', 'slug', 'usuario', 'url_ubicacion', 'horario', 'telefono']

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imagenes
        fields=['id', 'nombre_bares', 'url_imagen']

class BebidasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bebidas
        fields=['id', 'nombre', 'descripcion', 'precio', 'imagen', 'nombre_bar']

class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ofertas
        fields=['id', 'nombre', 'descripcion', 'precio', 'imagen', 'nombre_bar']