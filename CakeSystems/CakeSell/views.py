from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View
from .models import (Cliente, Venda, Estoque, Fornecedor)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *


def index(request):
    return render(request, 'index.html')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    fields = '__all__'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarCliente')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente/atualizar_cliente.html'

    def get_success_url(self):
        return reverse_lazy('listarCliente')



class VendaListView(ListView):
    model = Venda
    template_name = 'listar/venda.html'
    fields = '__all__'


class VendaCreateView(CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarVenda')


class EstoqueListView(ListView):
    model = Estoque
    template_name = 'listar/estoque.html'
    fields = '__all__'


class EstoqueCreateView(CreateView):
    model = Estoque
    template_name = 'cadastrar/estoque.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'listar/fornecedor.html'
    fields = '__all__'


class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'listar/fornecedor.html'
    fields = '__all__'


class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'atualizar/cliente/atualizar_cliente.html'

    def get_success_url(self):
        return reverse_lazy('listarCliente')


class VendaTamanhoBoloUpdateView(UpdateView):
    model = Venda
    form_class = VendaUpdateTamanhoBolo
    template_name = 'atualizar/venda/atualizar_tamanho_bolo_venda.html'

    def get_success_url(self):
        return reverse_lazy('listarVenda')

class VendaUpdateConcluidaView(UpdateView):
    model = Venda
    form_class = VendaUpdateConcluida
    template_name = 'atualizar/venda/atualizar_venda_concluida.html'

    def get_success_url(self):
        return reverse_lazy('listarVenda')


class FornecedorUpdateContatoView(UpdateView):
    model = Fornecedor
    form_class = FornecedorUpdateContato
    template_name = 'atualizar/fornecedor/atualizar_contato_fornecedor.html'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class FornecedorUpdateStatusView(UpdateView):
    model = Fornecedor
    form_class = FornecedorUpdateStatus
    template_name = 'atualizar/fornecedor/atualizar_status_fornecedor.html'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class EstoqueUpdateQuantidadeView(UpdateView):
    model = Estoque
    form_class = EstoqueUpdateQuantidade
    template_name = 'atualizar/estoque/atualizar_quantidade_estoque.html'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')


class EstoqueUpdateValorView(UpdateView):
    model = Estoque
    form_class = EstoqueUpdateValor
    template_name = 'atualizar/estoque/atualizar_valor_estoque.html'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')