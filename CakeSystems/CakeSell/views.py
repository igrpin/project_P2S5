from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View
from .models import Cliente, Venda
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    fields = '__all__'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cadastro_cliente.html'
    fields = '__all__'