
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Visita
from .forms import VisitaForm

class VentaListView(ListView):
    model = Visita
    template_name = 'ventas/venta_list.html'
    context_object_name = 'visitas'

class VentaDetailView(DetailView):
    model = Visita
    template_name = 'ventas/venta_detail.html'

class VentaCreateView(CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'ventas/venta_form.html'
    success_url = reverse_lazy('venta_list')