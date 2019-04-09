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
    


# Create your views here.
