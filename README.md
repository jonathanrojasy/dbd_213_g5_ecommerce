# E-Commerce

Aplicación web del E-Commerce de Vivanda. Proyecto final desarrollado para el curso de Diseño de Base de Datos de la Universidad Nacional de Ingeniería. 

### Pre-requisitos 📋

Necesitas tener instalado lo siguiente:

* Python 3.9.5 - [Ir a la página oficial](https://www.python.org/downloads/release/python-395/)


### Instalación 🔧

Para ejecutar la aplicación se requiere crear un entorno virtual en el que se instalará el software necesario para ejecutar la aplicación

Entorno virtual para Python

```
pip install virtualenv==20.13.2
```

Ahora valide que se instaló el paquete

> Aparecerán todos los paquetes instalados en su PC 

```
pip freeze
```

Crear el entorno virtual

_Para esto se debe crear una carpeta que contendrá las instalaciones_

> Crear la carpeta "entorno" y acceder a ella.

```
mkdir entorno
cd entorno
```

> Crear el entorno virtual llamado "init" y acceder a la carpeta "init/Scripts"

```
virtualenv init
cd init/Scripts
```

> Activar el entorno

```
activate
```

> Instalar Django 4.0.3

```
pip install Django==4.0.3
```

Validar que se haya instalado Django en el entorno

```
pip freeze
```

Regresar a la raíz del proyecto

> Ejecutar hasta llegar a la ruta donde se encuentra el archivo manage.py

```
cd ..
```



## Ejecutar en preproducción 📦

En la raiz en la que se encuentra el archivo manage.py ejecutar lo siguiente:

```
py manage.py runserver 
```

## Construido con 🛠️

* [Django 4.0](https://docs.djangoproject.com/en/4.0/) - El framework web usado


## Autores ✒️

* **Jonathan Rojas** - *Trabajo Inicial y Documentación* - [jonathanrojasy](https://github.com/jonathanrojasy)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/jonathanrojasy/dbd_213_g5_ecommerce/graphs/contributors) quíenes han participado en este proyecto. 