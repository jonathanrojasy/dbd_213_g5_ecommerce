from django.db import models

# Create your models here.


class Categoria(models.Model):
    id_departamento = models.CharField(max_length=10)
    id_categoria = models.CharField(max_length=10)
    name_cat = models.CharField(max_length=50)
    descripcion_categoria = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    '''class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']'''
    class Meta:
        managed = False
        db_table = 'categoria'


class Producto(models.Model):
    cod_producto = models.CharField(primary_key=True, max_length=10)
    nombre_producto = models.CharField(max_length=30)
    tipo_producto = models.CharField(max_length=50)
    marca_prod = models.CharField(max_length=30)
    informacion_producto = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=20)
    precio_unitario_producto = models.DecimalField(decimal_places=2, max_digits=9)
    id_sub_categoria = models.IntegerField()
    id_categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='id_categoria', null=True)
    id_departamento = models.IntegerField()
    cod_prom = models.CharField(max_length=20)
    
    class Meta:
        managed = False
        db_table = 'producto'


class Promocion(models.Model):
    cod_prom = models.CharField(max_length=20,primary_key=True)
    fecha_inicio_prom = models.DateField()
    fecha_fin_prom = models.DateField()
    desc_precio_producto = models.DecimalField(max_digits=9,decimal_places=2)
    tipo_prom = models.CharField(max_length=3)
    producto_regalo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'promocion'
