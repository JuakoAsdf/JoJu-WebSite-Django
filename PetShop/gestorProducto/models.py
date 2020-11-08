from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre        = models.TextField(max_length=50)
    activo        = models.BooleanField()

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre       = models.TextField(max_length=50)
    direccion    = models.TextField(max_length=100)
    telefono     = models.TextField(max_length=9)
    encargado    = models.TextField(max_length=60)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    marca        = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    categoria    = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    nombre       = models.TextField(max_length=60)
    codigo       = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion  = models.TextField(max_length = 200)
    stock        = models.IntegerField()
    precioCosto  = models.IntegerField()
    precioVenta  = models.IntegerField()

    def __str__(self):
        return self.nombre

class Adopcion(models.Model):
    nombre       = models.TextField(max_length=60)
    descripcion  = models.TextField(max_length = 200)
    activo        = models.BooleanField()

    def __str__(self):
        return self.nombre