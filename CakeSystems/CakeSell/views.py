from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from .models import (Cliente, Venda, Estoque, Fornecedor)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.decorators import login_required
from easy_pdf.views import PDFTemplateResponseMixin



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def index(request):
    return render(request, 'index.html')


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'listar/cliente.html'
    fields = '__all__'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cadastrar/cliente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarCliente')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'atualizar/cliente/atualizar_cliente.html'

    def get_success_url(self):
        return reverse_lazy('listarCliente')


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'detalhes/venda.html'


class VendaPDF(PDFTemplateResponseMixin, DetailView):
    model = Venda
    template_name = 'detalhes/venda_pdf.html'


class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'listar/venda.html'
    fields = '__all__'


class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'cadastrar/venda.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarVenda')


class EstoqueListView(LoginRequiredMixin, ListView):
    model = Estoque
    template_name = 'listar/estoque.html'
    fields = '__all__'


class EstoqueCreateView(LoginRequiredMixin, CreateView):
    model = Estoque
    template_name = 'cadastrar/estoque.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')


class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'listar/fornecedor.html'
    fields = '__all__'


class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'listar/fornecedor.html'
    fields = '__all__'


class FornecedorCreateView(LoginRequiredMixin, CreateView):
    model = Fornecedor
    template_name = 'cadastrar/fornecedor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'atualizar/cliente/atualizar_cliente.html'

    def get_success_url(self):
        return reverse_lazy('listarCliente')


class VendaTamanhoBoloUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    form_class = VendaUpdateTamanhoBolo
    template_name = 'atualizar/venda/atualizar_tamanho_bolo_venda.html'

    def get_success_url(self):
        return reverse_lazy('listarVenda')

class VendaUpdateConcluidaView(LoginRequiredMixin, UpdateView):
    model = Venda
    form_class = VendaUpdateConcluida
    template_name = 'atualizar/venda/atualizar_venda_concluida.html'

    def get_success_url(self):
        return reverse_lazy('listarVenda')


class FornecedorUpdateContatoView(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorUpdateContato
    template_name = 'atualizar/fornecedor/atualizar_contato_fornecedor.html'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class FornecedorUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorUpdateStatus
    template_name = 'atualizar/fornecedor/atualizar_status_fornecedor.html'

    def get_success_url(self):
        return reverse_lazy('listarFornecedor')


class EstoqueUpdateQuantidadeView(LoginRequiredMixin, UpdateView):
    model = Estoque
    form_class = EstoqueUpdateQuantidade
    template_name = 'atualizar/estoque/atualizar_quantidade_estoque.html'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')


class EstoqueUpdateValorView(LoginRequiredMixin, UpdateView):
    model = Estoque
    form_class = EstoqueUpdateValor
    template_name = 'atualizar/estoque/atualizar_valor_estoque.html'

    def get_success_url(self):
        return reverse_lazy('listarEstoque')

