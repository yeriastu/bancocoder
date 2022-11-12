from django.http import HttpResponse
from django.template  import Template, Context , loader



def empleado(request, nombre):
    
    documentoDeTexto = f' Mi nombre es: {" Erica y soy empleada"}'
    
    return HttpResponse(documentoDeTexto)




def probandoTemplate(request, nombre):
   
  #  miHtml = open(r'C:/Users/Lenovo/Desktop/ENTREGAFINAL/Databank/probanco/probanco/templates/templates1.html')
  #  plantilla = Template(miHtml.read())
  #  miHtml.close()
   
   
        
  #  mi_contexto = Context({"my_name": nombre, "notas": [6, 3, 8, 9]})
    
  #  documento = plantilla.render(mi_contexto)
    
    plantilla = loader.get_template("templates1.html")
    
    documento = plantilla.render({"my_name": nombre, "notas": [6, 3, 8, 9]})
    
    return HttpResponse(documento)
    
    


def producto(request):
    return HttpResponse("Soy tu Mejor Tarjeta de Credito")

def cliente(request):
    return HttpResponse("Vengo a pedir un credito a tasa fija") 