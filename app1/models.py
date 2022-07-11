from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)

    def __str__(self):
        return self.marca, self.modelo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    precio = models.IntegerField()
    

    def __str__(self):
        return self.nombre, self.marca, self.tipo, self.precio

class Album(models.Model):
    nombre = models.CharField(max_length=40)
    banda = models.CharField(max_length=40)
    year = models.IntegerField()
    

    def __str__(self):
        return self.nombre, self.banda, self.year
