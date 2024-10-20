from django.urls import path
from . import views

# app_name = 'compra'

# urlpatterns = [
#     path('', views.CompraListView.as_view(), name='compra_list'),
#     path('<int:pk>/', views.CompraDetailView.as_view(), name='compra_detail'),
#     path('nueva/', views.CompraCreateView.as_view(), name='compra_create'),
#     path('<int:pk>/editar/', views.CompraUpdateView.as_view(), name='compra_update'),
#     path('<int:pk>/eliminar/', views.CompraDeleteView.as_view(), name='compra_delete'),
#     path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
# ]

app_name = 'compra'

urlpatterns = [
    path('', views.CompraListView.as_view(), name='compra_list'),
    path('<int:pk>/', views.CompraDetailView.as_view(), name='compra_detail'),
    path('crear/', views.CompraCreateView.as_view(), name='compra_form'),
    path('editar/<int:pk>/', views.CompraUpdateView.as_view(), name='compra_update'),
    path('exportar-pdf/', views.exportar_compras_pdf, name='exportar_pdf'),
    path('buscar-cliente/', views.buscar_clientes, name='buscar_cliente'),
]