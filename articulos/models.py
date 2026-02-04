from django.db import models

# Create your models here.


class Articulo (models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    

    