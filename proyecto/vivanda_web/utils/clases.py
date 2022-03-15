
class Categoria:
    def __init__(self,tupla):
        self.id_categoria = tupla[0]
        self.descripcion_categoria = tupla[1]
        self.nombre_cat = tupla[2]
        self.id_departamento = tupla[3]

class Producto:
    def __init__(self,tupla):
        self.cod_producto = tupla[0]
        self.nombre_producto = tupla[1]
        self.tipo_producto = tupla[2]
        self.informacion_producto = tupla[3]
        self.unidad_medida = tupla[4]
        self.precio_unitario_producto = tupla[5]
        self.modelo_prod = tupla[6]
        self.marca_prod = tupla[7]
        self.id_sub_categoria = tupla[8]
        self.id_categoria = tupla[9]
        self.id_departamento = tupla[10]
        self.cod_prom = tupla[11]
