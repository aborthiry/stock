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


admin.site.register(Libro, LibroAdmin)
admin.site.register(PuntoDeVenta)
admin.site.register(Coleccion)
admin.site.register(Orden, OrdenAdmin)

