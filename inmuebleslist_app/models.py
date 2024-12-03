from django.db import models

# Create your models here.
class Edificacion(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen  = models.CharField( max_length=900)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre