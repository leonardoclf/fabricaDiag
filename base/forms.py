from django.forms import ModelForm
from base.models import Pacientes, diagnosticos, Prevencao


class PacientesForm(ModelForm):
    class Meta:
        model = Pacientes 
        fields = ['nome', 'dataNasc', 'genero', 'cpf', 'tipoSang', 'sintomas', 'descrCaso', 'gravidade', 'dataInc']

class diagnosticosForm(ModelForm):
    class Meta:
        model = diagnosticos
        fields = ['diagnostico']

class PrevencaoForm(ModelForm):
    class Meta:
        model = Prevencao
        fields = ['virus', 'prevenir']
    
