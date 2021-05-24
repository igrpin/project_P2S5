from django.contrib import admin
from .models import Venda, Cliente, FormaPagamento, RedeSocial, Massa, Recheio


# admin.site.register(Cliente)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "celular")


admin.site.register(Venda)
# admin.site.register(Bolo)
admin.site.register(Massa)
admin.site.register(Recheio)
admin.site.register(FormaPagamento)
admin.site.register(RedeSocial)
