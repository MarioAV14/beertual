from django.db import models
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

# Create your models here.

class Bares(models.Model):
    titulo_bar= models.CharField(max_length=50)
    logo_bar= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    descripcion_bar= models.CharField(max_length=250)
    slug= models.SlugField(unique=True, blank=True)
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_bar')
    url_ubicacion= models.URLField(max_length=200, blank=True, null=True)
    horario= models.CharField(max_length=50)
    telefono= models.CharField(max_length=10)
    def __str__(self):
        return self.titulo_bar

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Bares)

@receiver(post_save, sender=Bares)
def ensure_bares_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Bares.objects.get_or_create(bares=kwargs.get('instance'))

class Imagenes(models.Model):
    nombre_bares= models.ForeignKey("Bares", on_delete=models.CASCADE)
    url_imagen= models.URLField(max_length=200)
    def __str__(self):
        return self.nombre_bar

class Bebidas(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=250)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    nombre_bar= models.ForeignKey("Bares", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Ofertas(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=250)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    nombre_bar= models.ForeignKey("Bares", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre