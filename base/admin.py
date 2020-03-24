from django.contrib import admin
from .models import Pacientes, diagnosticos

# Register your models here.
admin.site.register(Pacientes)
admin.site.register(diagnosticos)
