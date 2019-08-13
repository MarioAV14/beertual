from rest_framework import serializers
from .models import Bares
from .models import Bebidas
from .models import Imagenes
from .models import Ofertas

class BaresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bares
        fields='__all__'

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Imagenes
        fields='__all__'

class BebidasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bebidas
        fields='__all__'

class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ofertas
        fields='__all__'

class OnlyNameBaresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bares
        fields=['titulo_bar','slug']
        
class GETOfertasSerializer(serializers.ModelSerializer):
    nombre_bar=OnlyNameBaresSerializer(read_only=True)
    class Meta:
        model=Ofertas
        fields='__all__'