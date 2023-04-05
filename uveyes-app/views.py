from django.http import HttpResponse
from .models import usuario
# Create your views here.

def init(request):
    return HttpResponse("<h1>UV EYES.</h1>")

def hello(request, user):
    try:
        usuario.objects.get(name=user)
    except:
        return HttpResponse("<h1>Usted no es un usuario registrado</h1>")
    else:
        return HttpResponse("<h1>Bienvenido %s.</h1>"%user)