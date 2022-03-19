from django.contrib import admin

# Register your models here.
from GestionPedidos.models import Producto, Categoria

admin.site.register([Categoria, Producto])