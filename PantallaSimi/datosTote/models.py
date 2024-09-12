from django.db import models

# Create your models here.

class Tote(models.Model):
  codigo = models.CharField(max_length=255)
  pallet = models.CharField(max_length=255)
  salida = models.CharField(max_length=255)
  destino = models.CharField(max_length=255)

class Producto(models.Model):
    sku = models.CharField(max_length=100)
    caja = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    detalle = models.TextField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.sku
