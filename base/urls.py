from django.urls import path
from . import views
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('', views.home, name="base-home"),
    path('accounts/login/', login_view),
    path('grafico/', views.grafico, name="grafico"),
    path('accounts/registro/', register_view, name="registro"),
    path('accounts/logout/', logout_view, name="logout"),
    path('cadpaciente', views.cadpaciente, name="base-cadpaciente"),   
    path('cadvirus', views.cadvirus, name="base-cadvirus"),   
    path('tratamento', views.tratamento, name="base-tratamento"),
    path('editar/<int:id>/', views.editar, name="base-editar"),
    path('apagar/<int:id>/', views.apagar, name="base-apagar"),
    path('editarp/<int:id>/', views.editarp, name="base-editarp"),
    path('apagarp/<int:id>/', views.apagarp, name="base-apagarp"),
]