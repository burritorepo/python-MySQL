from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from ReservaBarberia.forms import ReservaForm
from ReservaBarberia.models import Reserva

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
