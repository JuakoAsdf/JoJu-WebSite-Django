from django.contrib import admin
from .models import Marca
from .models import Categoria
from .models import Sucursal
from .models import Producto
from .models import Adopcion
# Register your models here.

class productoAdmin(admin.ModelAdmin):
    list_display   = ['nombre',
                      'precioVenta',
                      'descripcion',
                      'stock'] 

    list_display_filter = ['categoria',
                           'marca',
                           'precioVenta']
    search_fields       = ['nombre',
                           'descripcion']
admin.site.register(Producto, productoAdmin)                           
                           
class marcaAdmin(admin.ModelAdmin):
    list_display   = ['nombre']
    list_display_filter = ['nombre']   
admin.site.register(Marca, marcaAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display   = ['nombre','activo'] 
    list_display_filter = ['nombre']
    search_fields       = ['activo'] 
admin.site.register(Categoria, categoriaAdmin)

class sucursalAdmin(admin.ModelAdmin):
    list_display        = ['nombre', 
                           'direccion',
                           'telefono',
                           'encargado']
    list_display_filter = ['nombre']
    search_fields       = ['nombre',
                           'direccion']  
admin.site.register(Sucursal, sucursalAdmin)

admin.site.register(Adopcion)