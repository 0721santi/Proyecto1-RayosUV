from django.http import HttpResponse
from .models import usuario, busqueda
from django.shortcuts import render
# Create your views here.

def init(request):
    return render(request, 'index.html')

def hello(request, user):
    try:
        usuario.objects.get(name=user)
    except:
        return HttpResponse("<h1>Usted no es un usuario registrado</h1>")
    else:
        return HttpResponse("<h1>Bienvenido %s.</h1>"%user)

def historial(request):
    names = usuario.objects.all()
    busquedas = busqueda.objects.all()
    return render(request, 'historial.html', {
        'nombres':names,
        'busquedas':busquedas
    })