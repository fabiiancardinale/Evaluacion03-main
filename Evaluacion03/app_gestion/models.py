from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    ap_paterno=models.CharField(max_length=30)
    ap_materno=models.CharField(max_length=30)
    edad=models.IntegerField()
    vacuna=models.CharField(max_length=10)
    fecha=models.DateField(max_length=20)


class Vac_Domicilio(models.Model):
    rut=models.CharField(max_length=10)
    nombre_completo=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    comuna=models.CharField(max_length=30)
    telefono=models.IntegerField()