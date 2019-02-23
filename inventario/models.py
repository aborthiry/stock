from django.db import models

# Create your models here.

class Libro(models.Model):
    isbn = models.CharField(max_length=20,primary_key=True)
    coleccion = models.CharField(max_length=50)
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    paginas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    anio =  models.PositiveIntegerField()
    
class PuntoDeVenta(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class Stock(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    class Meta:
        unique_together = (("libro", "puntodeventa"),)


class Orden(models.Model):
    TIPO_DE_SALIDA = (
        ('1', 'Venta'),
        ('2', 'Distribución'),
        ('3', 'Donación'),
    )

    TIPO_DE_ENTRADA = (
        ('1', 'Impresión'),
        ('2', 'Distribución'),
    )
    
    salidapor = models.CharField(max_length=1, choices=TIPO_DE_SALIDA)
    entrada =  models.BooleanField(default=False)
    entradapor = models.CharField(max_length=1, choices=TIPO_DE_ENTRADA)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntodeventa = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    