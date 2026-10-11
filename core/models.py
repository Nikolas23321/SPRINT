from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def _str_(self):
        return self.nome
