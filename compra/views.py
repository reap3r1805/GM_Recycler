from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Compra, ProductoComprado
from cliente.models import Cliente
from cliente.forms import ClienteForm
from .forms import CompraForm
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from .utils import generar_pdf_compras
from django.contrib import messages
from django.forms import inlineformset_factory
from django.db import transaction


# class CompraListView(ListView):
#     model = Compra
#     template_name = 'compras/compra_list.html'
#     context_object_name = 'compras'

# class CompraDetailView(DetailView):
#     model = Compra
#     template_name = 'compras/compra_detail.html'

# class CompraCreateView(CreateView):
#     model = Compra
#     form_class = CompraForm
#     template_name = 'compras/compra_form.html'
#     success_url = reverse_lazy('compra_list')

# class CompraUpdateView(UpdateView):
#     model = Compra
#     form_class = CompraForm
#     template_name = 'compras/compra_form.html'
#     success_url = reverse_lazy('compra_list')

# class CompraDeleteView(DeleteView):
#     model = Compra
#     template_name = 'compras/compra_confirm_delete.html'
#     success_url = reverse_lazy('compra_list')

# def buscar_cliente(request):
#     query = request.GET.get('q', '')
#     clientes = Cliente.objects.filter(
#         Q(nombre__icontains=query) | Q(telefon__icontains=query)
#     )[:5]
#     data = [{'id': c.id, 'nombre': c.nombre, 'telefono': c.telefono} for c in clientes]
#     return JsonResponse(data, safe=False)
#     if query:
#         clientes = Cliente.objects.filter(
#             Q(nombre___icontains=query) | Q(telefono__icontains=query)
#         )
#     else:
#         clientes = Cliente.objects.none()
#     return render(request, 'compra/buscar_cliente.html', {
#         'clientes': clientes
#     })


class CompraListView(ListView):
    model = Compra
    paginate_by = 10
    template_name = 'compras/compra_list.html'

class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compras/compra_detail.html'

class CompraCreateView(SuccessMessageMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/compra_form.html'
    success_url = reverse_lazy('compra:lista')
    success_message = "Compra creada exitosamente con CCID: %(ccid)s"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductoCompradoFormSet = inlineformset_factory(Compra, ProductoComprado, fields=('imagen', 'cantidad', 'precio_unitario'), extra=1)
        if self.request.POST:
            context['formset'] = ProductoCompradoFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductoCompradoFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.save()
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            ccid=self.object.ccid,
        )

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error al crear la compra. Por favor, revisa los campos.")
        return super().form_invalid(form)

class CompraUpdateView(SuccessMessageMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/compra_update.html'
    success_url = reverse_lazy('compra:lista')
    success_message = "Compra actualizada exitosamente"

def exportar_compras_pdf(request):
    return generar_pdf_compras(request)

def buscar_clientes(request):
    query = request.GET.get('query', '')
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=query) | Q(telefono__icontains=query)
    )[:10]
    results = [{"id": c.id, "nombre": c.nombre, "telefono": c.telefono} for c in clientes]
    return JsonResponse({"results": results})