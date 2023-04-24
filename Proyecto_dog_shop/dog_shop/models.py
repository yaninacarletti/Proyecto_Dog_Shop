from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    num_max_citas = models.IntegerField()

    def __str__(self):
        return self.nombre
    


