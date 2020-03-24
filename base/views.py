from django.shortcuts import render, redirect
from .models import Pacientes, diagnosticos
from base.forms import PacientesForm, diagnosticosForm

def home(request):
    return render(request, 'base/home.html')

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

    
