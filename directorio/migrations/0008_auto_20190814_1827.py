# Generated by Django 2.2.4 on 2019-08-14 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0007_auto_20190814_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenes',
            old_name='nombre_bares',
            new_name='nombre_bar',
        ),
    ]
