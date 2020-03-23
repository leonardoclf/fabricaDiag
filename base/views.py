from django.shortcuts import render, redirect
from .models import Pacientes
from base.forms import PacientesForm

def home(request):
    return render(request, 'base/home.html')

def cadpaciente(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base-home')
    else:
        form = PacientesForm()
    return render(request, 'base/cadpaciente.html', {'form': form})

    
