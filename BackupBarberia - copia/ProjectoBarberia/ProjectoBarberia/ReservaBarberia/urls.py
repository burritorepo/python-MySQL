from django.urls import path, include
from .import views
from rest_framework import routers

from ReservaBarberia.views import RegistrarBarbero
from ReservaBarberia import views

routers = routers.DefaultRouter()
routers.register('ReservaBarberia', views.BarberoList)

app_name = "barberosapp"

urlpatterns = [
    path('registrarbarbero/', RegistrarBarbero.as_view(), name="registrar_barbero"),
    path('listarbarberos/', views.barberos_listado, name='listar_barberos')
]
