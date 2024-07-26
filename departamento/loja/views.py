from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse
# Create your views here.


# Retornando elementos apenas da categoria ferramentas
def ferramentas(request):
    produto = Produto.objects.filter(categoria__contains="Ferramentas")
    return HttpResponse(produto)


# Retornando com 0 estoque
def outEstoque(request):
    produto = Produto.objects.filter(quantidade="0")
    return HttpResponse(produto)



# Retornando com 0 estoque e categoria informatica
def outEstoqueInformatica(request):
    produto = Produto.objects.filter(categoria="Informatica", quantidade="0")
    return HttpResponse(produto)



# Retornando com peso entre 100g e 1000g
def peso(request):
    produto = Produto.objects.filter(peso__gte="100", peso__lte="1000")
    return HttpResponse(produto)



# Retornando todos os elementos com máximo de 5
def tudo(request):
    produto = Produto.objects.all()[0:5]
    return HttpResponse(produto)

