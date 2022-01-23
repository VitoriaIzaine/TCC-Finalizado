from django.db import models
from django.utils import timezone


class Depoimento(models.Model):
    nome = models.CharField(max_length=30)
    nota = models.CharField(max_length=30)
    # cidade = models.CharField(max_length=30)
    comentario = models.CharField(max_length=150)
    mostrar = models.BooleanField(default=True)


class Candidatar(models.Model):
    nome_candidado = models.CharField(max_length=50)
    data_nasc = models.DateField()
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade_c = models.CharField(max_length=30)
    id_vagaa = models.CharField(max_length=10,default='Não é preciso preencher',blank=True)

class Perfil_jovem(models.Model):
    data_nasc = models.DateField()
    cel_1 = models.CharField(max_length=20, blank=True, default='Se possuir preencher')
    tel = models.CharField(max_length=20, blank=True, default='Se possuir preencher')
    logradouro = models.CharField(max_length=50, default='Endereço')
    numero = models.CharField(max_length=20, default='Numero')
    bairro = models.CharField(max_length=50, default='Bairro')
    cidade_estado = models.CharField(max_length=50, default='Cidade/Estado')

    def __str__(self):
        return self.data_nasc
