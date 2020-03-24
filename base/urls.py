from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="base-home"),
    path('cadpaciente', views.cadpaciente, name="base-cadpaciente"),   
    path('cadvirus', views.cadvirus, name="base-cadvirus"),   
    path('editar/<int:id>/', views.editar, name="base-editar"),
    path('apagar/<int:id>/', views.apagar, name="base-apagar"),
]