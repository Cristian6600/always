from django.db import models

class Prueba(models.Model):
    hola = models.CharField(max_length=30)

class Contacto(models.Model):
    
    ASUNTO= ( 
    ("1", "Cotizacion"), 
    ("2", "Solicitud de informacion"), 
    
) 
    name = models.CharField(max_length=35)

    mail = models.EmailField(max_length=100)

    telefono = models.IntegerField()

    asunto = models.CharField(
        max_length=30,
        choices = ASUNTO,)

    mensaje = models.TextField(max_length=150)