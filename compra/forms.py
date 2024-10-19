from django import forms
from .models import Compra, DetalleCompra, Producto
from cliente.models import Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio_unitario']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente']
    
    detalles = forms.formset_factory(DetalleCompraForm, extra=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        if self.instance.pk:
            initial_detalles = [
                {'producto': detalle.producto, 
                 'cantidad': detalle.cantidad,
                 'precio_unitario': detalle.precio_unitario}
                 for detalle in self.instance.detallecompra_set.all()
            ]
            self.detalles = forms.formset_factory(DetalleCompraForm, extra=0)(initial=initial_detalles)

    def save(self, commit=True):
        compra = super().save(commit=False)
        if commit:
            compra.save()
            for form in self.detalles:
                if form.is_valid() and form.cleaned_data:
                    detalle = form.save(commit=False)
                    detalle.compra = compra
                    detalle.save()
        return compra
    

#ProductoFormSet = forms.inlineformset_factory(
    #Compra, Producto,form=ProductoForm,extra=1, can_delete=True)