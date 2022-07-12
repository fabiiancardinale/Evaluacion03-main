from django.shortcuts import render
from django.http import HttpResponse
from app_gestion.models import Persona, Vac_Domicilio

# Create your views here.
def ingresar_persona(request):
    return render(request, "ingresar_persona.html")

def listar(request):
    return render(request, "listar.html")

def index(request):
    return render(request, "index.html")

def busqueda_personas(request):
    return render(request, "busqueda_personas.html")

def registro_dom(request):
    return render(request, "registro_dom.html")

def eliminar_personas(request):
    return render(request, "eliminar_personas.html")

def ingreso_persona(request):
    rut_aux = request.GET["txt_rut"]
    nombre_aux = request.GET["txt_nombre"]
    apPaterno_aux = request.GET["txt_apPaterno"]
    apMaterno_aux = request.GET["txt_apMaterno"]
    edad_aux = request.GET["number_edad"]
    nombreVacuna_aux = request.GET["txt_vacuna"]
    fecha_aux = request.GET["fecha"]
    if len(nombre_aux)>0 and len(rut_aux)>0 and len(apPaterno_aux)>0 and len(apMaterno_aux)>0 and len(edad_aux)>0 and len(nombreVacuna_aux)>0 and len(fecha_aux)>0:
        pro = Persona(rut=rut_aux, nombre=nombre_aux,ap_paterno=apPaterno_aux,ap_materno=apMaterno_aux,edad=edad_aux, vacuna=nombreVacuna_aux, fecha=fecha_aux)
        pro.save()
        mensaje = "Persona Registrada"        
    else:
        mensaje = "Debe ingresar todos los datos"
    return render(request, 'listar.html')

def ingreso_dom(request):
    rut_aux = request.GET["txt_rut"]
    nombre_completo_aux = request.GET["txt_nombre_completo"]
    direccion_aux = request.GET["txt_direccion"]
    comuna_aux = request.GET["txt_comuna"]
    telefono_aux = request.GET["number_telefono"]
    if len(nombre_completo_aux)>0 and len(rut_aux)>0 and len(direccion_aux)>0 and len(comuna_aux)>0 and len(telefono_aux)>0:
        pro = Vac_Domicilio(rut=rut_aux, nombre_completo=nombre_completo_aux,direccion=direccion_aux,comuna=comuna_aux,telefono=telefono_aux)
        pro.save()    
    return render(request, 'listar.html')

def eliminacion_personas(request):
    if request.GET["txt_rut"]:
        rut_recibido =request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            pro = Persona.objects.get(rut=rut_recibido)
            pro.delete()
        return render(request, 'listar.html')
    
def listar_personas(request):
    datos = Persona.objects.all()
    return render(request, "listar.html",{'personas':datos})

def listar_domicilios(request):
    datos = Vac_Domicilio.objects.all()
    return render(request, "listar.html",{'Vac_Domicilios':datos})

def buscar(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=persona)
        return render(request, "buscado.html",{"personas":personas,"query":persona})
    else:
        mensaje = "Debe ingresar un rut"
        return HttpResponse(mensaje+"<br><a href='/index/'>Volver al inicio</a>")

