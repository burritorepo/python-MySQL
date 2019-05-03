from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from ReservaBarberia.forms import ReservaForm
from ReservaBarberia.models import Reserva,Barbero,Cliente
from django.core import serializers
from .serializer import BarberoSerializer
from rest_framework import viewsets

from django.template import RequestContext
from django.views.generic import CreateView
from django.urls import reverse_lazy

def home (request):
    context = {'foo': 'bar'}
    return render(request,'base.html',context)
    
def ejemplo(request):
    context = {'foo': 'bar'}
    titulo = 'Django vive en codigo'
    nombre = 'Pasando variables en Django'
    lista =[2,3,5,65,78,98,234,567,876]
    return render(request,'ejemplo.html',{'title':titulo,'nombre':nombre,'lista':lista},context)

""" Llamando el archivo index.html que representa
la plantilla de la aplicacion ReservaBarberia, que hereda su diseño de base.html """
def index (request):
    return render (request, 'reservas/index.html')

def reserva_view (request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'reservas/index.html',{'form':form})
    else:
        form = ReservaForm()
        return render(request,'reservas/reserva_form.html',{'form':form})

def reserva_list (request):
    reserva = Reserva.objects.all()
    context = {'reservas': reserva}
    return render(request,'reservas/reserva_list.html',context)

def reserva_edit (request,codres):
    reserva = Reserva.objects.get(codreserva=codres)
    if request.method == 'GET':
        form = ReservaForm(instance=reserva)
    else:
        form = ReservaForm(request.POST,instance=reserva)
        if form.is_valid():
            form.save()
            reserva = Reserva.objects.all()
            context = {'reservas': reserva}
            return render(request,'reservas/reserva_list.html',context)
    return render(request,'reservas/reserva_form.html',{'form':form})

def reserva_delete (request,codres):
    reserva = Reserva.objects.get(codreserva=codres)
    if request.method == 'POST':
        reserva.delete()
        reserva = Reserva.objects.all()
        context = {'reservas': reserva}
        return render(request,'reservas/reserva_list.html',context)
    return render(request,'reservas/reserva_delete.html',{'reserva':reserva})

# Create your views here.

def reservas_json(request):
    lista = serializers.serialize('json', Reserva.objects.all(),fields=['codbarbero','codclie'])
    return HttpResponse(lista,content_type='application/json')

class BarberoList(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializer_class = BarberoSerializer

class RegistrarBarbero(CreateView):
    template_name = 'barberos/barberos_registro.html'
    model = Barbero
    fields = ('barberonom','fecharegistro','description')
    success_url = reverse_lazy('barberos/barberos_registro.html')

    def post(self, request, *arg, **kwargs):
        estado = False
        barbero = Barbero()
        barbero.barberonom = request.POST['nombre']
        barbero.fecharegistro = request.POST['fecha']
        barbero.description = request.POST['descripcion']
        barbero.save()
        estado = True
        dic = {'estado': estado}
        contexto = {'barbero': barbero}
        return render(request, 'barberos/barberos_registro.html',dic,contexto)

class RegistrarCliente(CreateView):
    template_name = 'clientes/clientes_registro.html'
    model = Cliente
    fields = ('clientenom','telefono','fecharegistro','correo','imagen')
    success_url = reverse_lazy('clientes/clientes_registro.html')

    def post(self, request, *arg, **kwargs):
        estado = False
        cliente = Cliente()
        cliente.clientenom = request.POST['nombre']
        cliente.telefono = request.POST['telefono']
        cliente.fecharegistro = request.POST['fecha']
        cliente.correo = request.POST['correo']
        cliente.imagen = request.POST['imagen']
        cliente.save()
        estado = True
        dic = {'estado': estado}
        contexto = {'cliente': cliente}
        return render(request, 'clientes/clientes_registro.html',dic,contexto)

