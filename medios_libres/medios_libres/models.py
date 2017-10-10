from django.db import models

class Texto(models.Model):
    texto = models.TextField()

class Ubicacion(models.Model):
    lat = models.FloatField()
    longi = models.FloatField()
    usuario = models.CharField(max_length=50) # TODO model
    tiempo = models.DateTimeField(auto_now=True) # redundante?
