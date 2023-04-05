from django.db import models

# Create your models here.
class usuario(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class busqueda(models.Model):
    lugarbusqueda = models.CharField(max_length=50)
    resultado = models.FloatField(default=0)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        resultado = str(self.resultado)
        return resultado + ' - ' + self.usuario.name