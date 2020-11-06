from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.conf import settings
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
    return render(request,'adopcion.html', {})
    
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