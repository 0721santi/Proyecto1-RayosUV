from django import forms

class registro(forms.Form):
    usuario = forms.CharField(label="Nombre de usuario",max_length=100)
    contrasena = forms.CharField(label="Contraseña", max_length=50)
    nombre = forms.CharField(label="Tu nombre", max_length=30)
    apellido = forms.CharField(label="Tu apellido", max_length=40)
    ciudad = forms.CharField(label="Tu ciudad", max_length=50)
    edad = forms.IntegerField(label="Tu edad")
class inicio(forms.Form):
    usuario = forms.CharField(label="Usuario",max_length=100)
    contrasena = forms.CharField(label="Contraseña", max_length=50)
class busqueda(forms.Form):
    posicion = forms.CharField(label="Posicion de busqueda",max_length=100)
