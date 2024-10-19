from django.db import models
from django.utils import timezone
from tkinter import CASCADE

class TipoCliente(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    teléfono = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    dirección = models.CharField(max_length=200, blank=False, null=False, default="N/A")
    número_identificación_vehículo = models.CharField(max_length=17, blank=False, null=False, default="N/A")
    año_fabricación_vehículo = models.PositiveIntegerField(blank=False, null=False, default=2000)
    modelo_vehículo = models.CharField(max_length=100, blank=False, null=False, default="N/A")
    marca_vehículo = models.CharField(max_length=100, blank=False, null=False, default="N/A")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, default="2")

    def __str__(self):
        return self.nombre

