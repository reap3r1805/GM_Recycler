from django import forms
from .models import Compra, ProductoComprado
from cliente.models import Cliente


# class ProductoForm(forms.ModelForm):
#     class Meta:
#         model = Producto
#         fields = ['nombre', 'imagen', 'precio']
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#             'imagen': forms.FileInput(attrs={'class': 'form-control'}),
#             'precio': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# class DetalleCompraForm(forms.ModelForm):
#     class Meta:
#         model = DetalleCompra
#         fields = ['producto', 'cantidad', 'precio_unitario']
#         widgets = {
#             'producto': forms.TextInput(attrs={'class': 'form-control'}),
#             'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
#             'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# class CompraForm(forms.ModelForm):
#     class Meta:
#         model = Compra
#         fields = ['cliente']
#         widgets = {
#             'cliente': forms.Select(attrs={'class': 'form-control'}),
#         }
    
#     detalles = forms.formset_factory(DetalleCompraForm, extra=1)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cliente'].queryset = Cliente.objects.all()
#         if self.instance.pk:
#             initial_detalles = [
#                 {'producto': detalle.producto, 
#                  'cantidad': detalle.cantidad,
#                  'precio_unitario': detalle.precio_unitario}
#                  for detalle in self.instance.detallecompra_set.all()
#             ]
#             self.detalles = forms.formset_factory(DetalleCompraForm, extra=0)(initial=initial_detalles)

#     def save(self, commit=True):
#         compra = super().save(commit=False)
#         if commit:
#             compra.save()
#             for form in self.detalles:
#                 if form.is_valid() and form.cleaned_data:
#                     detalle = form.save(commit=False)
#                     detalle.compra = compra
#                     detalle.save()
#         return compra
    

# #ProductoFormSet = forms.inlineformset_factory(
#     #Compra, Producto,form=ProductoForm,extra=1, can_delete=True)

class ProductoCompradoForm(forms.ModelForm):
    class Meta:
        model = ProductoComprado
        fields = ['imagen', 'cantidad', 'precio_unitario']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

ProductoCompradoFormSet = forms.inlineformset_factory(
    Compra, ProductoComprado, form=ProductoCompradoForm, extra=1, can_delete=True
)