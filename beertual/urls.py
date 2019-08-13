from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from directorio.views import *

directorio=routers.DefaultRouter()

directorio.register('registros-de-bebidas',BebidasViewSet)
directorio.register('registros-de-bares',BaresViewSet)
directorio.register('registros-de-ofertas',OfertasViewSet)
directorio.register('registros-de-imagenes',ImagenesViewSet)
directorio.register('get-ofertas',GETOfertasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directorio/', include(directorio.urls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    )
]