from django.db import models

# Create your models here.
class Inmueble(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen  = models.CharField( max_length=900)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.direccion