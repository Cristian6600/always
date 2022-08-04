from django.db import models

class Prueba(models.Model):
    hola = models.CharField(max_length=30)
