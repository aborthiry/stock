from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

from pprint import pprint


# Create your models here.

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'


class Libro(models.Model):
    isbn = models.CharField(max_length=20,primary_key=True)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.PROTECT,verbose_name="Colección",)
    autor = models.CharField(max_length=100)
    titulo = models.CharField("Título",max_length=200)
    paginas = models.PositiveIntegerField("Páginas")
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    anio =  models.PositiveIntegerField("Año")
    def __str__(self):
        return self.titulo
    
class PuntoDeVenta(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField("Dirección", max_length=50)
    telefono = models.CharField("Teléfono", max_length=50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Punto de Venta'
        verbose_name_plural = 'Puntos de Venta'


class Stock(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.PROTECT,verbose_name="Punto de venta")
    cantidad = models.PositiveIntegerField()
    class Meta:
        unique_together = (("libro", "puntodeventa"),)
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'




TIPO_DE_ORDEN = (
        ('1', 'Salida - Venta'),
        ('2', 'Salida - Distribución'),
        ('3', 'Salida - Donación'),
        ('4', 'Entrada - Impresión'),
        ('5', 'Entrada - Distribución'),
)

class TipoOrden(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
   

class OrdenClasificada(models.Model):
    tipoorden = models.ForeignKey(TipoOrden, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    


class Orden(models.Model):
    
    tipodeorden = models.CharField("Tipo de orden", max_length=1, choices=TIPO_DE_ORDEN,default='1')
    '''  tipoorden = models.ForeignKey(TipoOrden,on_delete=models.PROTECT)
    ordenclasificada = ChainedForeignKey(
        OrdenClasificada,
        chained_field="tipoorden",
        chained_model_field="tipoorden",
        show_all=False,
        auto_choose=True,
        blank=True, null=True,
        on_delete=models.PROTECT) '''
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.PROTECT,verbose_name="Punto de venta")
    cantidad = models.PositiveIntegerField()
    nota = models.TextField(blank=True, null=True)
    fechaorden =  models.DateTimeField(auto_now_add=True, blank=False)
    added_by = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.fechaorden)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'





  
    