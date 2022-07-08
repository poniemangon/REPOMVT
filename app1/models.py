from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)

    def __str__(self):
        return self.marca, self.modelo
