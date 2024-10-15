from django.db import models
from django.utils import timezone
from cliente.models import Cliente

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    fecha_venta = models.DateTimeField(default=timezone.now)
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Venta de {self.cliente.nombre} el {self.fecha_venta.strftime('%d/%m/%Y')}"

class ProductoVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='productos')
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre_producto} - Venta {self.venta.id}"

    def subtotal(self):
        return self.cantidad * self.precio_unitario