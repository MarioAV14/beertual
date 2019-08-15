from django.db import models
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

# Create your models here.

class Bar(models.Model):
    titulo_bar= models.CharField(max_length=50,blank=True, null=True)
    logo_bar= models.ImageField(upload_to='logos')
    descripcion_bar= models.TextField(blank=True, null=True)
    slug= models.SlugField(unique=True, blank=True)
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_bar')
    url_ubicacion= models.URLField(blank=True, null=True)
    horario= models.CharField(max_length=50, blank=True, null=True)
    telefono= models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.titulo_bar

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Bar)

@receiver(post_save, sender=Bar)
def ensure_bares_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Bar.objects.get_or_create(titulo_bar=kwargs.get('instance'))

class Imagenes(models.Model):
    nombre_bar= models.ForeignKey("Bar", on_delete=models.CASCADE)
    url_imagen= models.ImageField(upload_to='imagenesbares')
    def __str__(self):
        return self.nombre_bar.titulo_bar

class Bebidas(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True, null=True)
    precio= models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    imagen= models.ImageField(upload_to='imagenbebidas',blank=True, null=True)
    nombre_bar=models.ForeignKey("Bar", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Ofertas(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True, null=True)
    precio= models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    imagen= models.ImageField(upload_to='imagenofertas',blank=True, null=True)
    nombre_bar=models.ForeignKey("Bar", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre