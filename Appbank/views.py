from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Produtos, Cliente
# Create your views here.

def empleado(request, nombre, apellido, documento, legajo):
    
   empleado = Empleado(nombre=nombre, apellido=apellido, documento=documento, legajo=legajo) 
   
   empleado.save()
   
   return HttpResponse(f"""
    <p>Empleado:{empleado.nombre} - Legajo{empleado.legajo} bienvenido ! </p>
    """)
   
def lista_empleados(request):
       
    lista = Empleado.objects.all 
    
    return render(request, "lista_empleados.html", {"lista_empleados": lista }) 