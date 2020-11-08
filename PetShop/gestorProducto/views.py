from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.conf import settings
from gestorProducto.models import Adopcion
from gestorProducto.models import Producto
# Create your views here.

def inicio(request):
    
    return render(request,'inicio.html', {})
    
def alimentoadultocat(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Comida Gato Adulto")

    contexto = {'lista' : lista}   
    return render(request,'alimentoadultocat.html', contexto)
    
def alimentogatito(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Comida Gatito")

    contexto = {'lista' : lista}   
    return render(request,'alimentogatito.html', contexto)

def accesoriocat(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Accesorios Gatos")

    contexto = {'lista' : lista}  
    return render(request,'accesoriocat.html', contexto)
    
def alimentoadultodog(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Comida Perro Adulto")

    contexto = {'lista' : lista}   
    return render(request,'alimentoadultodog.html', contexto)

def alimentocachorro(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Comida Cachorrito")

    contexto = {'lista' : lista}  
    return render(request,'alimentocachorro.html', contexto)

def accesoriodog(request):
    lista = {}
    
    if request.method == "POST":
        nombre        = request.POST["txtNombre"]
        descripcion   = request.POST["txtDescripcion"]
        
        if 'btnListar' in request.POST:
            lista = Producto.objects.filter(categoria__nombre = "Accesorios Perros")

    contexto = {'lista' : lista} 
    return render(request,'accesoriodog.html', contexto)
    
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
    if request.method == "POST":
        nombre = request.POST["txtUsuario"]
        correo  = request.POST["txtCorreo"]    
        clave  = request.POST["txtClave"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request,'login.html', {})