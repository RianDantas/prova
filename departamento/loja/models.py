from django.db import models

# Create your models here.

class Produto(models.Model):
    categoria = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    preco = models.IntegerField(default=0)
    quantidade = models.CharField(max_length=100)
    peso = models.IntegerField(default=0)

    def __str__(self):
        return self.categoria + self.nome + self.quantidade 