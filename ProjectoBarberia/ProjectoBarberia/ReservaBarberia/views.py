from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
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

# Create your views here.
