from django.http import HttpResponse
from .models import usuario, busqueda
from django.shortcuts import render, redirect
from .forms import registro, inicio, busqueda
import requests
import json
# Create your views here.

def init(request):
    return render(request, 'index.html')
def reguser(request):
    return render(request, 'loggedin.html')
def historial(request):
    return render(request, 'backend/historial.html')
def busqueda(request):
    if request.method == 'GET':
        return render(request, 'backend/busqueda.html', {
        "form": busqueda()
    })
    else:
        url = "https://google-maps-geocoding3.p.rapidapi.com/geocode"
        querystring = {"address":request.POST['posicion']}
        headers = {
	        "X-RapidAPI-Key": "9b5f56befdmsh35a4a3652de3a8bp1926f7jsnc2eb2fb639a5",
	        "X-RapidAPI-Host": "google-maps-geocoding3.p.rapidapi.com"
        }       
        response = requests.get(url, headers=headers, params=querystring)
        t = response.json()
        lat = t['latitude']
        lon = t['longitude']
        HttpResponse("<h1>Estás en ",request.POST['posicion']," que equivale a: Latitud ",lat," y longitud ",lon)
        return redirect('../loggedin.html')
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
#def posreq(request):
#    url = "https://google-maps-geocoding3.p.rapidapi.com/geocode"
#    querystring = {"address":"Medellin"}
#    headers = {
#	    "X-RapidAPI-Key": "9b5f56befdmsh35a4a3652de3a8bp1926f7jsnc2eb2fb639a5",
#	    "X-RapidAPI-Host": "google-maps-geocoding3.p.rapidapi.com"
#    }
#    response = requests.get(url, headers=headers, params=querystring)
#    t = response.json()
#    lat = t['latitude']
#    lon = t['longitude']
#    return HttpResponse(lat, lon)
#
#def uvIndex(request):
#    try:
#        url = "https://uv-index3.p.rapidapi.com/uv-index"
#
#        querystring = {"lat":"6.2476376","lon":"-75.5658153"}
#
#        headers = {
#	        "X-RapidAPI-Key": "9b5f56befdmsh35a4a3652de3a8bp1926f7jsnc2eb2fb639a5",
#	        "X-RapidAPI-Host": "uv-index3.p.rapidapi.com"
#        }
#
#        response = requests.get(url, headers=headers, params=querystring)
#
#        print(response.json())
#    except:
#        return HttpResponse("<h1>Usuario incorrecto</h1>")
