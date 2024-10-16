from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False, default="N/A")
    numero_identificacion_vehiculo = models.CharField(max_length=17, blank=False, null=False, default="N/A")
    anio_fabricacion_vehiculo = models.PositiveIntegerField(blank=False, null=False, default=2000)
    modelo_vehiculo = models.CharField(max_length=100, blank=False, null=False, default="N/A")
    marca_vehiculo = models.CharField(max_length=100, blank=False, null=False, default="N/A")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre