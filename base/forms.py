from django.forms import ModelForm
from base.models import Pacientes




class PacientesForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome', 'dataNasc', 'genero', 'cpf', 'tipoSang', 'sintomas', 'descrCaso', 'gravidade', 'dataInc']
