from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# # Create your models here.

class Profile(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_usuario')
    nombre= models.CharField(max_length=50)
    ap_paterno= models.CharField(max_length=50)
    ap_materno= models.CharField(max_length=50,blank=True, null=True)
    correo= models.EmailField(max_length=254)
    num_telefono= models.CharField(max_length=10)
    foto= models.ImageField(upload_to='imagenusuario', blank=True, null=True)
    slug= models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.usuario.username

    @property
    def username(self):
        return self.usuario.username

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Profile)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=kwargs.get('instance'))

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)