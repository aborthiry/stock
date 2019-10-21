from django.contrib import admin

# Register your models here.
from .models import Libro
from .models import PuntoDeVenta
from .models import Coleccion
from .models import Orden
from .models import Stock
#from .models import OrdenClasificada


class LibroAdmin(admin.ModelAdmin):
    # ...
    list_display = ('titulo', 'autor','precio','coleccion')
    search_fields = ('titulo', 'autor')
    list_filter = ('precio',)

class OrdenAdmin(admin.ModelAdmin):
    # ...
    name = 'Ordenes'
    list_display = ('libro', 'puntodeventa','tipodeorden','cantidad','fechaorden','added_by')
    #search_fields = ('libro','puntodeventa')
    list_filter = ('libro','puntodeventa','fechaorden',)
    exclude = ['added_by',]
    actions = None # no hay acciones sobre este modelo para mantener la coherecia del stock vs ordenes

    def save_model(self, request, obj, form, change):
        # con combo de tipo de orden fijo
        cantidadaux = 0
        try:
            stock = Stock.objects.get(libro=obj.libro,puntodeventa=obj.puntodeventa)
        except Stock.DoesNotExist:
            stock = None
        
        if stock is not None: # ya existe el stock, lo actulizo
            cantidadaux = obj.cantidad
            if int(obj.tipodeorden) < 3: # orde de salida por ende descuento
                cantidadaux = obj.cantidad * -1

            stock.cantidad = stock.cantidad + cantidadaux 
            stock.save()
        else:
            Stock.objects.create(libro=obj.libro, puntodeventa=obj.puntodeventa,cantidad=obj.cantidad)


        #agrego quien hace la carga de la orden
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user            
        super().save_model(request, obj, form, change)  

class ColeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PuntoDeVentaAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','telefono',)

class StockAdmin(admin.ModelAdmin):
    # ...
    list_display = ('libro', 'puntodeventa','cantidad')
    #search_fields = ('libro',)
    list_filter = ('puntodeventa','libro',)
    actions = None

    #no permite agregar al stock direcamente, debe usar una orden
    #def has_add_permission(self, request, obj=None):
    #    return False
    
    

#class OrdenClasificadaAdmin(admin.ModelAdmin):
 #   list_display = ('tipoorden','nombre',)



admin.site.register(Libro, LibroAdmin)
admin.site.register(PuntoDeVenta, PuntoDeVentaAdmin)
admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Stock, StockAdmin)
#admin.site.register(OrdenClasificada, OrdenClasificadaAdmin)

#cambia el admin 
admin.site.site_header = 'Control de Inventario Editorial UNICEN'
admin.site.site_title = 'Editorial Unicen'



