from django.db import models

# Create your models here.
class usuario(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)