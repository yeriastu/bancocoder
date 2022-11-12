from django.db import models 

# Create your models here.
class Empleado(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    legajo = models.IntegerField()
    
 
class Productos(models.Model):
    
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    nro_cuenta = models.IntegerField()