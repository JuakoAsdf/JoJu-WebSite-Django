from django.shortcuts import render
from gestorProducto.models import Adopcion
# Create your views here.

def inicio(request):
    return render(request,'inicio.html', {})
    
def alimentoadultocat(request):
    return render(request,'alimentoadultocat.html', {})
    
def alimentogatito(request):
    return render(request,'alimentogatito.html', {})

def accesoriocat(request):
    return render(request,'accesoriocat.html', {})
    
def alimentoadultodog(request):
    return render(request,'alimentoadultodog.html', {})

def alimentocachorro(request):
    return render(request,'alimentocachorro.html', {})

def accesoriodog(request):
    return render(request,'accesoriodog.html', {})
    
def adopcion(request):
    mensaje = "";
    lista = {}
    item = {}
    
    if request.method == "POST":
        id            = int("0" + request.POST["txtId"])
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        activo        = request.POST.get("chkActivo") is "1" 
        
        if 'btnGrabar' in request.POST:
        
            if id < 1: 
                Adopcion.objects.create(nombre = nombre, descripcion = descripcion, activo = activo) #registra los datos
            else:
                item = Adopcion.objects.get(pk = id)
                item.nombre = nombre
                item.descripcion = descripcion
                item.activo = activo
                item.save() #guarda los cambios
                item = {}
            
            mensaje = "Datos guardados"

        elif 'btnBuscar' in request.POST:
            try:
                item = Adopcion.objects.get(pk = id) 
            except:
                mensaje = "Registro no encontrado"
                item = {}
                
             
        elif 'btnListar' in request.POST:
            lista = Adopcion.objects.all()
        
        elif 'btnEliminar' in request.POST:
            item = Adopcion.objects.get(pk = id) #obtiene el registro segun id
            
            if isinstance(item, Adopcion):
                item.delete()
                mensaje = "Registro eliminado"
                item = {}
                
    contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item}
    return render(request,'adopcion.html', contexto)
    
def nosotros(request):
    return render(request,'nosotros.html', {})
    
def login(request):
    return render(request,'login.html', {})