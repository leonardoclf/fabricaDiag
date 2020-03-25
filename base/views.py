from django.shortcuts import render, redirect, get_object_or_404
import json
from django.contrib.auth.decorators import login_required
from .models import Pacientes, diagnosticos, Prevencao
from base.forms import PacientesForm, diagnosticosForm, PrevencaoForm
from accounts.views import login_view


@login_required
def home(request):
    context = {
        'Pacientes': Pacientes.objects.all(),
        'diagnosticos': diagnosticos.objects.all(),
    }
    return render(request, 'base/home.html', context)

def cadpaciente(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        diag_form = diagnosticosForm(request.POST)
        if form.is_valid() and diag_form.is_valid():
            Pacientes = form.save()
            Diag = diag_form.save(commit=False) 
            Diag.Pacientes = Pacientes
            diag_form.save()
            return redirect('base-home')
    else:
        form = PacientesForm()
        diag_form = diagnosticosForm()    
    context = {'form': form, 'diag_form': diag_form}    
    return render(request, 'base/cadpaciente.html', context)

def editar(request, id):
    paciente = get_object_or_404(Pacientes, pk=id)
    form = PacientesForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect("base-home")
    return render(request, "base/editar.html", {'form': form})    

def cadvirus(request):
    # Isso aqui conserta o bug do {form:form}
    form = PrevencaoForm()
    if request.method == 'POST':
        form = PrevencaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base-home')
        else:
            form = PrevencaoForm()
    return render(request, 'base/cadvirus.html', {'form': form})


def apagar(request, id):
    paciente = get_object_or_404(Pacientes, pk=id)
    if request.method == "POST":
        paciente.delete()
        return redirect('base-home')
    return render(request, 'base/apagar.html', {'paciente': paciente})

def tratamento(request):
    context = {
        'Prevencao': Prevencao.objects.all(),
    }
    return render(request, 'base/tratamento.html', context)

def editarp(request, id):
    prevencao = get_object_or_404(Prevencao, pk=id)
    form = PrevencaoForm(request.POST or None, instance=prevencao)
    if form.is_valid():
        form.save()
        return redirect("base-tratamento")
    return render(request, "base/editarp.html", {'form': form})

def apagarp(request, id):
    prevencao = get_object_or_404(Prevencao, pk=id)
    if request.method == "POST":
        prevencao.delete()
        return redirect('base-tratamento')
    return render(request, 'base/apagarp.html', {'prevencao': prevencao})

def grafico(request):
    pacientes = Pacientes.objects.all()
    diagnosticosAll = diagnosticos.objects.all()
    
    numDiagnosticos = {d.diagnostico:0 for d in diagnosticosAll}

    for p in pacientes:
        print(p.nome)
        numDiagnosticos[p.diagnosticos.diagnostico] = numDiagnosticos[p.diagnosticos.diagnostico] + 1
    
    x = list(numDiagnosticos.keys())
    x.sort()
    y = [numDiagnosticos[d] for d in x]

    context = {
        'x': json.dumps(x),
        'y': json.dumps(y)
    }
    return render(request, 'base/grafico.html', context)





 

        



    
