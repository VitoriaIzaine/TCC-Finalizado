from django import forms
from empresa.models import Vagas
from empresa.models import Perfil_empresa


class VagasForm(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = ['titulo', 'descricao', 'local', 'requisitos', 'resposabilidades', 'beneficios', 'empresa']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil_empresa
        fields = ['celular_1', 'celular_2', 'telefone', 'logradouro', 'numero', 'bairro',
                  'cidade_estado']
