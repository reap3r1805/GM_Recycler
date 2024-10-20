from django.db import models
from django.utils import timezone
from tkinter import CASCADE
from cliente.models import Cliente


# class Producto(models.Model):
#     nombre = models.CharField(max_length=100)
#     imagen = models.ImageField(upload_to='media/imagen/', null=True, blank=True)
#     precio = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.nombre
    
# class Compra(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     ccid = models.CharField(max_length=20, unique=True, editable=False)
#     fecha_creación = models.DateTimeField(default=timezone.now)
#     productos = models.ManyToManyField(Producto, through='DetalleCompra')

#     def save(self, *args, **kwargs):
#         if not self.ccid:
#             self.ccid = self.generar_ccid()
#         super().save(*args, **kwargs)

#     def generar_ccid(self):
#         hoy = timezone.now()
#         prefijo = f"FTE{hoy.strftime('%d%m%Y')}"
#         ultima_compra = Compra.objects.filter(ccid__startswith=prefijo).order_by('-ccid').first()
#         if ultima_compra:
#             ultimo_numero = int(ultima_compra.ccid[-4:])
#             nuevo_numero = f"{ultimo_numero + 1:04d}"
#         else:
#             nuevo_numero = "0001"
#         return f"{prefijo}{nuevo_numero}"
    
#     def __str__(self):
#         return f"Compra {self.ccid}"
    
# class DetalleCompra(models.Model):
#     compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField(default=1)
#     precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

#     class Meta:
#         unique_together = ('compra', 'producto')

#     def __str__(self):
#         return f"{self.cantidad} x {self.producto.nombre} en {self.compra.ccid}"



class Compra(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    ccid = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.ccid:
            self.ccid = self.generar_ccid()
        super().save(*args, **kwargs)

    def generar_ccid(self):
        hoy = timezone.now()
        prefijo = f"FTE{hoy.strftime('%d%m%Y')}"
        
        ultima_compra = Compra.objects.filter(
            ccid__startswith=prefijo
        ).order_by('-ccid').first()

        if ultima_compra:
            ultimo_numero = int(ultima_compra.ccid[-4:])
            nuevo_numero = ultimo_numero + 1
        else:
            nuevo_numero = 1

        return f"{prefijo}{nuevo_numero:04d}"

    def __str__(self):
        return f"Compra {self.ccid} - {self.cliente}"

class ProductoComprado(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='compras/')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario