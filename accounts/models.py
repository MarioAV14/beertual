# from django.db import models

# # Create your models here.

# class Profile(models.Model):
#     usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_usuario')
#     slug= models.SlugField(unique=True, blank=True)
#     cumple=models.DateField(blank= True, null=True)
#     def __str__(self):
#         return self.usuario.username

#     @property
#     def username(self):
#         return self.usuario.username

# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# pre_save.connect(rl_pre_save_receiver, sender=Profile)

# @receiver(post_save, sender=User)
# def ensure_profile_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         Profile.objects.get_or_create(usuario=kwargs.get('instance'))
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)