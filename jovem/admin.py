from django.contrib import admin
from .models import Depoimento
from .models import Candidatar
from .models import Perfil_jovem


@admin.register(Depoimento)
class detDepoimento(admin.ModelAdmin):
    list_display = ['nome', 'nota', 'comentario']


@admin.register(Candidatar)
class detCandidatar(admin.ModelAdmin):
    list_display = ['nome_candidado', 'data_nasc', 'rua', 'numero', 'bairro', 'cidade_c', 'id_vagaa']


@admin.register(Perfil_jovem)
class detperfilJovem(admin.ModelAdmin):
    list_display = ['data_nasc', 'cel_1', 'tel', 'logradouro', 'numero', 'bairro', 'cidade_estado']
