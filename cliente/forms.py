from django import forms
from .models import Cliente, TipoCliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 
            'teléfono', 
            'email', 
            'dirección', 
            'número_identificación_vehículo', 
            'año_fabricación_vehículo', 
            'modelo_vehículo', 
            'marca_vehículo', 
            'tipo_cliente',
            ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'teléfono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dirección': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'número_identificación_vehículo': forms.TextInput(attrs={'class': 'form-control'}),
            'año_fabricación_vehículo': forms.NumberInput(attrs={'class': 'form-control'}),
            'modelo_vehículo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_vehículo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-control'}),
        }