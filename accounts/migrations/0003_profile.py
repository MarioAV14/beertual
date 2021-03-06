# Generated by Django 2.2.4 on 2019-08-14 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('ap_paterno', models.TextField()),
                ('ap_materno', models.TextField(blank=True, null=True)),
                ('correo', models.EmailField(max_length=254)),
                ('num_telefono', models.CharField(max_length=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenusuario')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
