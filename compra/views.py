from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Compra, Producto
from cliente.models import Cliente
from cliente.forms import ClienteForm
from .forms import CompraForm
from django.db.models import Q


class CompraListView(ListView):
    model = Compra
    template_name = 'compras/compra_list.html'
    context_object_name = 'compras'

class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compras/compra_detail.html'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/compra_form.html'
    success_url = reverse_lazy('compra_list')

class CompraUpdateView(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/compra_form.html'
    success_url = reverse_lazy('compra_list')

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/compra_confirm_delete.html'
    success_url = reverse_lazy('compra_list')

def buscar_cliente(request):
    query = request.GET.get('q', '')
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=query) | Q(telefon__icontains=query)
    )[:5]
    data = [{'id': c.id, 'nombre': c.nombre, 'telefono': c.telefono} for c in clientes]
    return JsonResponse(data, safe=False)
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre___icontains=query) | Q(telefono__icontains=query)
        )
    else:
        clientes = Cliente.objects.none()
    return render(request, 'compra/buscar_cliente.html', {
        'clientes': clientes
    })

