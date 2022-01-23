from django import forms
from jovem.models import Depoimento
from jovem.models import Candidatar
from jovem.models import Perfil_jovem


class DepoimentoForm(forms.ModelForm):
    class Meta:
        model = Depoimento
        fields = ['nome', 'nota', 'comentario']


class CandidatarForm(forms.ModelForm):
    class Meta:
        model = Candidatar
        fields = ['nome_candidado', 'data_nasc', 'rua', 'numero', 'bairro', 'cidade_c', 'id_vagaa']

