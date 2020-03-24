from django.db import models
from django.utils import timezone

# Create your models here.
class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    dataNasc = models.DateField() 
    genero = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    tipoSang = models.CharField(max_length=50)
    sintomas = models.CharField(max_length=150)
    descrCaso = models.TextField() 
    gravidade = models.CharField(max_length=50)
    dataInc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

# Extensão da tabela de pacientes. Um paciente terá um diagnosticos
class diagnosticos(models.Model):
    Pacientes = models.OneToOneField(Pacientes, on_delete=models.CASCADE)
    diagnosticos_escolha = (
        ("Covid-19", "Covid-19"),
        ("Influenza", "Influenza"),
        ("Influenza H1N1", "Influenza H1N1"),
        ("Influenza H5N1", "Influenza H5N1"),
    )
    diagnostico = models.CharField(max_length=50, choices=diagnosticos_escolha)
    def __str__(self):
        return self.Pacientes.nome







    
