from django.contrib import admin
from .models import Pacientes, diagnosticos, Prevencao

# Register your models here.
admin.site.register(Pacientes)
admin.site.register(diagnosticos)
admin.site.register(Prevencao)
