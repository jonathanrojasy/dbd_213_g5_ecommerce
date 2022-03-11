from django.shortcuts import render
from . models import Producto

# Create your views here.
def index(request):
    categorias = Producto.objects.raw('SELECT c.id_categoria id, c.* FROM categoria as c;')
    productos = Producto.objects.raw('SELECT p.cod_producto id, p.* FROM producto as p;')
    # FORMATEAR PRODUCTOS
    arrProductos = []
    for categoria in categorias:
        dictAxu = {}
        dictAxu[categoria.id_categoria] = []
        arrProductos.append(dictAxu)
    for categoria in categorias:
        for producto in productos:
            if producto.id_categoria == categoria.id_categoria:
                count = 0
                for categProd in arrProductos:
                    key_list = list(categProd.keys())
                    categoryAux = key_list[0]
                    if categoryAux == categoria.id_categoria:
                        arrProductos[count][categoryAux].append(producto)
                    count += 1

    return render(request, 'productos/index.html',{'categorias': categorias, 'productos': arrProductos })

def demo(request):
    productos = Producto.objects.raw('SELECT p.cod_producto id, p.* FROM producto as p;')
    return render(request, 'productos/demoRead.html',{'productos': productos})