from django.db import models


class Vagas(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)
    mostrar = models.BooleanField(default=True)
    local = models.CharField(max_length=30, default='Campinas')
    requisitos = models.CharField(max_length=100)
    resposabilidades = models.CharField(max_length=100)
    beneficios = models.CharField(max_length=100)
    empresa = models.CharField(max_length=50, blank=True, default='Não preencher')

    def __str__(self):
        return self.empresa


class Perfil_empresa(models.Model):
    celular_1 = models.CharField(max_length=20, blank=True, default='Se possuir preencher')
    celular_2 = models.CharField(max_length=20, blank=True, default='Se possuir preencher')
    telefone = models.CharField(max_length=20, blank=True, default='Se possuir preencher')
    logradouro = models.CharField(max_length=50, default='Endereço')
    numero = models.CharField(max_length=20, default='Numero')
    bairro = models.CharField(max_length=50, default='Bairro')
    cidade_estado = models.CharField(max_length=50, default='Cidade/Estado')

    def __str__(self):
        return self.celular_1
