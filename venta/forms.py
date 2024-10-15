from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'importe_total']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'importe_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }