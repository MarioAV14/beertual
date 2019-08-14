# Generated by Django 2.2.4 on 2019-08-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='status',
            field=models.CharField(choices=[('Atendido', 'Atendido'), ('No Atendido', 'No Atendido'), ('Citado', 'Citado'), ('Venta', 'Venta'), ('Llamado', 'Llamado'), ('Ingresado', 'Ingresado'), ('No Venta', 'No Venta')], default='No Atendido', max_length=11),
        ),
    ]
