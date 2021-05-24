from django.contrib import admin
from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
)

urlpatterns = [
    path('listar/cliente', ClienteListView.as_view(), name="listarCliente"),
    path('cadastrar/cliente', ClienteCreateView.as_view(), name="cadastrarCliente"),
]
