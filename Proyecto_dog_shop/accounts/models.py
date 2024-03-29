from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= 'avatares', null =True, blank=True)

    # def __str__(self):
    #     return self.user


class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=250)
    mensaje = models.CharField(max_length=1000)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.correo


