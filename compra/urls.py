from django.urls import path
from . import views

app_name = 'compra'

urlpatterns = [
    path('', views.CompraListView.as_view(), name='compra_list'),
    path('<int:pk>/', views.CompraDetailView.as_view(), name='compra_detail'),
    path('nueva/', views.CompraCreateView.as_view(), name='compra_create'),
    path('<int:pk>/editar/', views.CompraUpdateView.as_view(), name='compra_update'),
    path('<int:pk>/eliminar/', views.CompraDeleteView.as_view(), name='compra_delete'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
]