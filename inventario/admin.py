from django.contrib import admin

# Register your models here.
from .models import Libro
from .models import PuntoDeVenta
from .models import Coleccion
from .models import Orden


class LibroAdmin(admin.ModelAdmin):
    # ...
    list_display = ('titulo', 'autor','precio','coleccion')
    search_fields = ('titulo', 'autor')
    list_filter = ('precio',)

class OrdenAdmin(admin.ModelAdmin):
    # ...
    list_display = ('libro', 'puntodeventa','cantidad','fechaorden')
    search_fields = ('libro',)
    list_filter = ('fechaorden',)

class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PuntoDeVentaAdmin(admin.ModelAdmin):
    list_display = ('telefono',)



admin.site.register(Libro, LibroAdmin)
admin.site.register(PuntoDeVenta, PuntoDeVentaAdmin)
admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Orden, OrdenAdmin)

#cambia el admin 
admin.site.site_header = 'Control de Inventario Editorial UNICEN'
admin.site.site_title = 'Editorial Unicen'



