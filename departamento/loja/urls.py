from django.urls import path
from . import views

urlpatterns = [
    path("ferramentas/", views.ferramentas),
    path("outestoque/", views.outEstoque),
    path("outestoqueinformatica/", views.outEstoqueInformatica),
    path("peso/", views.peso),
    path("tudo/", views.tudo),
]