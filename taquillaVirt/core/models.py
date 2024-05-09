from django.db import models

class Espectaculo(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField()
    productor = models.CharField(max_length=100)