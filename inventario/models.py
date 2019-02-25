from django.db import models

# Create your models here.

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    isbn = models.CharField(max_length=20,primary_key=True)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    paginas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    anio =  models.PositiveIntegerField()
    def __str__(self):
        return self.titulo
    
class PuntoDeVenta(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Stock(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    class Meta:
        unique_together = (("libro", "puntodeventa"),)


TIPO_DE_ORDEN = (
        ('1', 'Salida - Venta'),
        ('2', 'Salida - Distribución'),
        ('3', 'Salida - Donación'),
        ('4', 'Entrada - Impresión'),
        ('5', 'Entrada - Distribución'),
)

class Orden(models.Model):
    
    tipodeorden = models.CharField(max_length=1, choices=TIPO_DE_ORDEN,default='1')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    nota = models.TextField(blank=True, null=True)
    fechaorden =  models.DateTimeField(auto_now_add=True, blank=False)
    
    def __str__(self):
        return str(self.fechaorden)
    