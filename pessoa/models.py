from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uf = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.nome_completo



















