from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=8)
    descripcion_categoria = models.CharField(max_length=64)
    nombre_cat = models.IntegerField()
    id_departamento = models.IntegerField()

class Producto(models.Model):
    cod_producto = models.CharField(max_length=8)
    nombre_producto = models.CharField(max_length=64)
    tipo_producto = models.CharField(max_length=64)
    informacion_producto = models.CharField(max_length=300)
    unidad_medida = models.CharField(max_length=200)
    precio_unitario_producto = models.FloatField()
    id_marca = models.CharField(max_length=8)
    id_categoria = models.CharField(max_length=8)
