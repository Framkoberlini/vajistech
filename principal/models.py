from django.db import models
from django.contrib.auth.models import User


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=500)
    precio = models.CharField(max_length=100)
    detalle_url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.usuario.username} - {self.nombre}"