from django import forms
from .models import *


class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class VendaUpdateTamanhoBolo(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['tamanhoBolo']


class VendaUpdateConcluida(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendaConcluida']


class FornecedorUpdateContato(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nomeDoContato']


class FornecedorUpdateStatus(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['statusFornecedor']


class EstoqueUpdateQuantidade(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['quantidade']

class EstoqueUpdateValor(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['valor']
