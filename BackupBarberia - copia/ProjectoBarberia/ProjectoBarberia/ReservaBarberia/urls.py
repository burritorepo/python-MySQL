from django.urls import path, include
from .import views
from rest_framework import routers

from ReservaBarberia.views import RegistrarBarbero, RegistrarCliente, reserva_delete, reserva_edit, reserva_list, reserva_view
from ReservaBarberia import views

routers = routers.DefaultRouter()
routers.register('ReservaBarberia', views.BarberoList)

app_name = "barberosapp"

urlpatterns = [
    path('registrarbarbero/', RegistrarBarbero.as_view(), name='registrar_barbero'),
    path('listarbarberos/', views.barberos_listado, name='listar_barberos'),
    path('registrocliente/',RegistrarCliente.as_view(),name='registrar_cliente'),
    path('listado/',views.reservas_json,name='listado'),
    path('listar/',views.reserva_list,name='reserva_list'),
    path('nuevo/',views.reserva_view,name='reserva_view'),
    path('editar/<codres>/',views.reserva_edit,name='reserva_edit'),
    path('delete/<codres>/',views.reserva_delete,name='reserva_delete')
    
]
