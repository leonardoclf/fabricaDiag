from django.db import models
from django.utils import timezone

# Create your models here.
class Pacientes(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    dataNasc = models.DateField(verbose_name="Data do Nascimento") 
    genero = models.CharField(max_length=50, verbose_name="Gênero do Paciente")
    cpf = models.CharField(max_length=50, verbose_name="Número do CPF")
    tipoSang = models.CharField(max_length=50, verbose_name="Tipo Sanguíneo")
    sintomas = models.CharField(max_length=150, verbose_name="Sintomas")
    descrCaso = models.TextField(verbose_name="Descrição do Caso") 
    gravidade = models.CharField(max_length=50, verbose_name="Grau de Gravidade")
    dataInc = models.DateTimeField(default=timezone.now, verbose_name="Data do Cadastro")

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

class Prevencao(models.Model):
    virus = models.CharField(max_length=50)
    prevenir = models.TextField()

    def __str__(self):
        return self.virus






    
