from django.contrib import admin
from .models import Vagas
from .models import Perfil_empresa


@admin.register(Vagas)
class detVagas(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'local', 'requisitos', 'resposabilidades', 'beneficios', 'empresa']


@admin.register(Perfil_empresa)
class detPerfilEmpresa(admin.ModelAdmin):
    list_display = ['celular_1', 'celular_2', 'telefone', 'logradouro', 'numero', 'bairro',
                    'cidade_estado']
