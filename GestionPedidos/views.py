
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from GestionPedidos.Carrito import Carrito
from GestionPedidos.models import Producto, Promocion
from GestionUsuarios.Usuario import Cliente
from vivanda_web.conexion import conexion


def add_product(request, sku):
    cart = Carrito(request)
    product = get_object_or_404(Producto, pk=sku)
    if product.cod_prom:
        prom = get_object_or_404(Promocion, pk=product.cod_prom)
        cart.agregar(product, prom)
    else:
        cart.agregar(product)
    return redirect("/productos")


def remove_product(request, sku):
    cart = Carrito(request)
    product = get_object_or_404(Producto, pk=sku)
    cart.eliminar(product)
    return redirect("listado_productos")


def decrement_product(request, sku):
    cart = Carrito(request)
    product = get_object_or_404(Producto, pk=sku)
    cart.restar(product)
    return redirect("/productos")


def clear_cart(request):
    cart = Carrito(request)
    cart.limpiar()
    return redirect("listado_productos")


def principal(request):
    return render(request, 'principalProducto.html', {'bebida': 'liquor'})


def listado_productos(request):
    products = Producto.objects.order_by('sku')
    return render(request, "tienda.html", {"products": products})


def finalizar(request):
    cart = Carrito(request)
    client = Cliente(request)
    inserts = ''
    try:
        with conexion:
            with conexion.cursor() as cursor:
                for key1, value1 in request.session.get("cliente").items():
                    for key, value in request.session.get("carrito").items():
                        inserts = '''INSERT INTO pedido (id_pedido,fecha_creacion_pedido,hora_creacion_pedido,id_usuario) 
                                    VALUES (nextval('SEQ01'),CURRENT_DATE,CURRENT_TIME,'%s');
                                    INSERT INTO orden_pedido (id_pedido,cod_producto,cantidad,precio_unitario,descuento)
                                    VALUES (currval('SEQ01'),'%s',%s,%s,%s);''' %(value1["id_usuario"],value["producto_id"],value["cantidad"],value["precio"],value["descuento"])
                cursor.execute(inserts)
    except Exception as e:
        return HttpResponse(e)
    cart.limpiar()
    return redirect('index')


def listaPedidos(request):
    try:
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute('''SELECT PE.ID_PEDIDO, PE.FECHA_CREACION_PEDIDO, OP.PRECIO_UNITARIO*OP.CANTIDAD AS MONTO
                                FROM PEDIDO PE, ORDEN_PEDIDO OP
                                WHERE PE.ID_PEDIDO=OP.ID_PEDIDO group by PE.ID_PEDIDO,PE.FECHA_CREACION_PEDIDO;''')
                registro = cursor.fetchall()
                if registro:
                    return render(request, 'listaPedidos.html', {'registro': registro})
                else:
                    return HttpResponse('No hay pedidos')
    except Exception as e:
        return HttpResponse('error: %' %(e,))
