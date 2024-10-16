from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 
            'telefono', 
            'email', 
            'direccion', 
            'numero_identificacion_vehiculo', 
            'anio_fabricacion_vehiculo', 
            'modelo_vehiculo', 
            'marca_vehiculo', 
            ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'numero_identificacion_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio_fabricacion_vehiculo': forms.NumberInput(attrs={'class': 'form-control'}),
            'modelo_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
        }