from django.contrib import admin
from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    VendaCreateView,
    VendaListView,
    EstoqueCreateView,
    EstoqueListView,
    FornecedorCreateView,
    FornecedorListView,
    ClienteUpdateView,
    VendaTamanhoBoloUpdateView,
    VendaUpdateConcluidaView,
    FornecedorUpdateContatoView,
    FornecedorUpdateStatusView,
    EstoqueUpdateQuantidadeView,
    EstoqueUpdateValorView,
)


urlpatterns = [
    path('listar/cliente', ClienteListView.as_view(), name="listarCliente"),
    path('cadastrar/cliente', ClienteCreateView.as_view(), name="cadastrarCliente"),
    path('listar/venda', VendaListView.as_view(), name="listarVenda"),
    path('cadastrar/venda', VendaCreateView.as_view(), name="cadastrarVenda"),
    path('listar/estoque', EstoqueListView.as_view(), name="listarEstoque"),
    path('cadastrar/estoque', EstoqueCreateView.as_view(), name="cadastrarEstoque"),
    path('listar/fornecedor', FornecedorListView.as_view(), name="listarFornecedor"),
    path('cadastrar/fornecedor', FornecedorCreateView.as_view(), name="cadastrarFornecedor"),
    path('atualizar/cliente/<int:pk>', ClienteUpdateView.as_view(), name="atualizarCliente"),
    path('atualizar/tamanho_bolo_venda/<int:pk>', VendaTamanhoBoloUpdateView.as_view(), name="atualizarVendaTamanhoBolo"),
    path('atualizar/venda_concluida/<int:pk>', VendaUpdateConcluidaView.as_view(), name="atualizarVendaConcluida"),
    path('atualizar/status/fornecedor/<int:pk>', FornecedorUpdateStatusView.as_view(), name="atualizarStatusFornecedor"),
    path('atualizar/contato/fornecedor/<int:pk>', FornecedorUpdateContatoView.as_view(), name="atualizarContatoFornecedor"),
    path('atualizar/quantidade/estoque/<int:pk>', EstoqueUpdateQuantidadeView.as_view(), name="atualizarQuantidadeEstoque"),
    path('atualizar/valor/estoque/<int:pk>', EstoqueUpdateValorView.as_view(), name="atualizarValorEstoque"),
]

