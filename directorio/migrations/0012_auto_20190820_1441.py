# Generated by Django 2.2.4 on 2019-08-20 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0011_auto_20190820_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_bar', to=settings.AUTH_USER_MODEL),
        ),
    ]
