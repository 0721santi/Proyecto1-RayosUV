from django.http import HttpResponse
from .models import usuario, busqueda
from django.shortcuts import render, redirect
from .forms import registro, inicio
# Create your views here.

def init(request):
    return render(request, 'index.html')
def reguser(request):
    return render(request, 'loggedin.html')
def historial(request):
    return render(request, 'backend/historial.html')
def login(request):
    if request.method == 'GET':
        return render(request, 'backend/inicio.html', {
        "form": inicio()
    })
    else:
        try:
            usuario.objects.get(surname=request.POST['usuario'], password=request.POST['contrasena'])
        except:
            HttpResponse("<h1>Usuario incorrecto</h1>")
            return redirect('inicio.html')
        else:
            return redirect('../loggedin.html')
        
def singup(request):
    if request.method == 'GET':
        return render(request, 'backend/registro.html', {
        "form": registro()
    })
    else:
        usuario.objects.create(surname=request.POST['usuario'],password=request.POST['contrasena'], name=request.POST['nombre'], lastname=request.POST['apellido'], location=request.POST['ciudad'], age=request.POST['edad'])
        return redirect('../loggedin.html')

