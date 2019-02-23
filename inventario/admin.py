from django.contrib import admin

# Register your models here.
from .models import Libro
from .models import PuntoDeVenta

admin.site.register(Libro)
admin.site.register(PuntoDeVenta)