from django.shortcuts import render
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
    return render(request,'login.html', {})