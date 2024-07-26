from django.contrib import admin
from .models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nome', 'preco', 'quantidade' , 'peso')

admin.site.register(Produto, ProdutoAdmin)
