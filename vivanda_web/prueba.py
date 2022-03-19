from conexion import conexion
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE USUARIO SET PASSWORD='jeimy' WHERE nombre_usuario='jeimy';")
except Exception as e:
    print(e)