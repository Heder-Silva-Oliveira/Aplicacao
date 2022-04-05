from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome_completo















