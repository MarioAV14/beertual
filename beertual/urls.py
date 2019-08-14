from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from directorio.views import *
from rest_framework.authtoken import views
from accounts.views import UserViewSet
from accounts.views import ProfileViewSet
from contacto.views import EmpresaViewSet

directorio=routers.DefaultRouter()
accounts=routers.DefaultRouter()
contacto=routers.DefaultRouter()

directorio.register('registros-de-bebidas',BebidasViewSet)
directorio.register('registros-de-bares',BaresViewSet)
directorio.register('registros-de-ofertas',OfertasViewSet)
directorio.register('registros-de-imagenes',ImagenesViewSet)
directorio.register('get-ofertas',GETOfertasViewSet)
accounts.register('registro-perfiles',ProfileViewSet)
contacto.register('resgistro-de-empresas',EmpresaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directorio/', include(directorio.urls)),
    path('accounts/', include(accounts.urls)),
    path('contacto/', include (contacto.urls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]