from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.conf import settings
from gestorProducto.models import Adopcion
from gestorProducto.models import Producto
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
# Create your views here.

def logout(request):
    return redirect('')
    
def inicio(request):
    return render(request,'inicio.html', {})
                  
def buscar(request):
    item = {}
    
    if request.method == "POST":
        buscar = request.POST['txtBuscar']
        
        if 'txtBuscar' in request.POST:
            item = Producto.objects.filter(nombre__contains = buscar,
                                          descripcion__contains = buscar)
        
    return render(request,'buscar.html', {'item': item})
    
def alimentoadultocat(request):
    lista = Producto.objects.filter(categoria__nombre = "Comida Gato Adulto")
    contexto = {'lista' : lista}   
    return render(request,'alimentoadultocat.html', contexto)
    
def alimentogatito(request):
    lista = Producto.objects.filter(categoria__nombre = "Comida Gatito")
    contexto = {'lista' : lista}   
    return render(request,'alimentogatito.html', contexto)

def accesoriocat(request):
    lista = Producto.objects.filter(categoria__nombre = "Accesorios Gatos")
    contexto = {'lista' : lista}  
    return render(request,'accesoriocat.html', contexto)
    
def alimentoadultodog(request):
    lista = Producto.objects.filter(categoria__nombre = "Comida Perro Adulto")
    contexto = {'lista' : lista}   
    return render(request,'alimentoadultodog.html', contexto)

def alimentocachorro(request):
    lista = Producto.objects.filter(categoria__nombre = "Comida Cachorrito")
    contexto = {'lista' : lista}  
    return render(request,'alimentocachorro.html', contexto)

def accesoriodog(request):
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
        activo        = request.POST.get("chkActivo") == "1" 
        
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

def loginPage(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['username']
            clave = form.cleaned_data['password']                
            user = authenticate(username=nombre, password=clave)
            
            if user is not None:
                do_login(request, user)
                return redirect('inicio')    
    return render(request,'loginn.html', {'form':form})
    
def registerPage(request):
    if request.method == "POST":
        nombre = request.POST["txtUsuario"]
        correo  = request.POST["txtCorreo"]    
        clave  = request.POST["txtClave"]
        User.objects.create(username=nombre, email=correo, password=make_password(clave))
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request,'register.html', {})
    

    
