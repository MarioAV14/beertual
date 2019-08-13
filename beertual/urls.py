from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from directorio.views import BaresViewSet
from directorio.views import BebidasViewSet
from directorio.views import OfertasViewSet
from directorio.views import ImagenesViewSet

directorio=routers.DefaultRouter()

directorio.register('registros-de-bebidas',BebidasViewSet)
directorio.register('registros-de-bares',BaresViewSet)
directorio.register('registros-de-ofertas',OfertasViewSet)
directorio.register('registros-de-imagenes',ImagenesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directorio/', include(directorio.urls))
]