import json
from decimal import Decimal


class fakefloat(float):
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)

def defaultencode(o):
    if isinstance(o, Decimal):
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto, promocion=None):
        if producto.cod_producto not in self.carrito.keys():
            descuento = 0
            if promocion:
                try:
                    descuento = float(json.dumps(promocion.desc_precio_producto, default=defaultencode))
                except:
                    pass
            
                
            self.carrito[producto.cod_producto] = {
                "producto_id": producto.cod_producto,
                "nombre": producto.nombre_producto,
                "cantidad": 1,
                "precio": float(json.dumps(producto.precio_unitario_producto, default=defaultencode)),
                "acumulado": float(json.dumps(producto.precio_unitario_producto, default=defaultencode)),
                "descuento": descuento,
                "marca": producto.marca_prod
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.cod_producto):
                    value["cantidad"] += 1
                    value["acumulado"] += value["precio"]
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        sku = producto.cod_producto
        if sku in self.carrito:
            del self.carrito[sku]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == producto.cod_producto:
                value["cantidad"] -= 1
                value["acumulado"] -= value["precio"]
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                else:
                    self.guardar_carrito()
                break
            else:
                print("El producto no existe en el carrito")

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
