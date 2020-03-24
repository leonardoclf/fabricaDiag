from django.shortcuts import render, redirect, get_object_or_404
from .models import Pacientes, diagnosticos, Prevencao
from base.forms import PacientesForm, diagnosticosForm, PrevencaoForm

def home(request):
    context = {
        'Pacientes': Pacientes.objects.all()
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

def editar(request, id):
    paciente = get_object_or_404(Pacientes, pk=id)
    form = PacientesForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect("base-home")
    return render(request, "base/editar.html", {'form': form})

def apagar(request, id):
    paciente = get_object_or_404(Pacientes, pk=id)
    if request.method == "POST":
        paciente.delete()
        return redirect('base-home')
    return render(request, 'base/apagar.html', {'paciente': paciente})






    
