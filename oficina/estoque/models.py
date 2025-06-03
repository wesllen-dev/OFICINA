from django.db import models

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    localizacao = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
