from django.db import models

# Create your models here.

class Empresa   (models.Model):
    ATENDIDO='Atendido'
    NO_ATENDIDO='No Atendido'
    CITADO='Citado'
    VENTA='Venta'
    LLAMADO='Llamado'
    INGRESADO='Ingresado'
    NO_VENTA='No Venta'
    status_choices = [
        (ATENDIDO, 'Atendido'),
        (NO_ATENDIDO, 'No Atendido'),
        (CITADO, 'Citado'),
        (VENTA, 'Venta'),
        (LLAMADO, 'Llamado'),
        (INGRESADO, 'Ingresado'),
        (NO_VENTA, 'No Venta'),
    ]
    nombre= models.CharField(max_length=50)
    correo= models.EmailField(max_length=254)
    num_telefono= models.CharField(max_length=10, blank=True, null=True)
    status= models.CharField(max_length=11, choices=status_choices, default=NO_ATENDIDO)
    def __str__(self):
        return self.nombre