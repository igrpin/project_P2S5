from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Venda(models.Model):
    massa = models.ManyToManyField('Massa', blank=False, verbose_name='Sabor da massa')
    recheio = models.ManyToManyField('Recheio', blank=False, verbose_name='Recheio')
    tamanhoBolo = [
        ('Mini', 'Mini'),
        ('PP', 'PP'),
        ('Pequeno', 'P'),
        ('Médio', 'M'),
        ('Grande', 'G'),
    ]
    tamanhoBolo = models.CharField(
        max_length=7
        , choices=tamanhoBolo
        , blank=False
        , null=False
        ,
    )
    qtdeVenda = models.IntegerField(blank=False, null=False, verbose_name='Quantidade')
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False,
                                verbose_name='Valor total do pedido')
    dataVenda = models.DateField(auto_now_add=True, blank=True, null=False)
    horaVenda = models.TimeField(auto_now_add=True, blank=True, null=False)
    formaPagamento = models.ManyToManyField('FormaPagamento', blank=True, verbose_name='Forma de pagamento')
    parcelado = models.BooleanField(null=False, blank=False, default=False, verbose_name='Parcelado?')
    qtdeParcelas = models.IntegerField(null=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.DO_NOTHING, default=1, verbose_name='Cliente', blank=True)
    vendaConcluida = models.BooleanField(blank=False, null=False, default=True, verbose_name='Venda concluída')
    excluido = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return str(self.pk) + ' - ' + self.cliente.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome completo')
    celular = models.CharField(max_length=11, blank=False, null=False, verbose_name='Celular')
    email = models.EmailField(blank=True, null=False, verbose_name='E-mail')
    perfilRedeSocial = models.CharField(max_length=255, blank=True, null=True, verbose_name='Perfil')
    redeSocial = models.ForeignKey('RedeSocial', verbose_name='Rede social', blank=True, null=True, on_delete=models.DO_NOTHING)
    dataNascimento = models.DateField(blank=False, null=False, verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=11, blank=True, verbose_name='CPF')
    foto = models.FileField(upload_to='foto_cliente/', null=True, blank=True)

    def __str__(self):
        return str(self.pk) + ' - ' + self.nome



class Massa(models.Model):
    tipoMassa = models.CharField(max_length=255, blank=False, null=False, verbose_name='Tipo de massa')

    def __str__(self):
        return str(self.pk) + ' - ' + self.tipoMassa


class Recheio(models.Model):
    tipoRecheio = models.CharField(max_length=255, blank=False, null=False, verbose_name='Recheio')


    def __str__(self):
        return str(self.pk) + ' - ' + self.tipoRecheio


class FormaPagamento(models.Model):
    formaPagamento = models.CharField(null=False, blank=False, max_length=255, verbose_name='Forma de pagamento', default='Dinheiro')

    def __str__(self):
        return str(self.pk) + ' - ' + self.formaPagamento


class RedeSocial(models.Model):
    titulo = models.CharField(null=False, blank=False, max_length=255, verbose_name='Rede Social')
    urlPrincipal = models.CharField(null=False, blank=False, max_length=255, verbose_name='URL Principal')

    def __str__(self):
        return self.titulo

class Estoque(models.Model):
    produto = models.CharField(max_length=255, null=False, blank=False, verbose_name='Produto')
    quantidade = models.IntegerField(blank=True, null=False, default=0, verbose_name='Quantidade de entrada')
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.DO_NOTHING, verbose_name='Fornecedor', blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, verbose_name='Valor do produto')
    marca = models.CharField(max_length=255, null=False, blank=False, verbose_name='Marca')
    codigoDeBarra = models.CharField(max_length=13, null=False, blank=False, verbose_name='Código de barra')
    dataInclusaoProduto = models.DateField(auto_now_add=True, blank=False, null=False, verbose_name='Data de inclusão')

    def __str__(self):
        return self.produto



class Fornecedor(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Código Fornecedor')
    razaoSocial = models.CharField(max_length=255, null=False, blank=False, verbose_name='Razão social')
    cnpj = models.CharField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    email = models.EmailField(blank=True, null=True)
    nomeDoContato = models.CharField(max_length=255, blank=True, verbose_name='Nome do contato na empresa')
    liberado = models.BooleanField(blank=True, null=False, default=False)
    status = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    ]
    statusFornecedor = models.CharField(
        max_length=7
        , choices=status
        , blank=False
        , null=False
        ,
    )


    def __str__(self):
        return self.razaoSocial


