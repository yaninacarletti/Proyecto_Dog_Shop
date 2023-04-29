from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to= 'productos', null =True, blank=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    num_max_citas = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to= 'servicios', null =True, blank=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):

    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'marcas', null =True, blank=True)

    def __str__(self):
        return self.nombre
    
class LeerMasServicios(models.Model):

    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    imagen = models.ImageField(upload_to= 'leerMasServicios', null =True, blank=True)

    def __str__(self):
        return self.titulo