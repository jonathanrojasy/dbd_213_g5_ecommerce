# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    tipo_documento = models.CharField(max_length=2, choices=[('D','DNI'),('R','RUC')], blank=False, null=False)
    cod_documento = models.CharField(max_length=13, blank=False, null=False)
    genero = models.CharField(max_length=2,choices=[('M','Masculino'),('F','Femenino')],blank=True,null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    correo_electronico = models.CharField(max_length=40, blank=False, null=False)
    password = models.CharField(max_length=32, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'usuario'