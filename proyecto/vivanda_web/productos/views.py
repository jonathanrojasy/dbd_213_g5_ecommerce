from django.shortcuts import render

# Create your views here.
def index(request):
    categorias = [
        {
            'nombre': 'Packs',
            'id': 'packs'
        }, 
        {
            'nombre': 'Carnes, Aves y Pescados',
            'id': 'cayp'
        }, 
        {
            'nombre': 'Frutas y Verduras',
            'id': 'fyv'
        }
    ]
    productos = [
        {
            'packs': [
                {'nombre': 'Six Pack Heineken','id': 'p0001'},
                {'nombre': 'Six Pack Agua San Mateo','id': 'p0002'},
                {'nombre': 'Six Pack Yogurt','id': 'p0003'},
                {'nombre': 'Six Pack Gaseosa Coca Cola','id': 'p0004'},
            ]
        },
        {
            'cayp': [
                {'nombre': 'Carne de res','id': 'p0005'},
                {'nombre': 'Pavo','id': 'p0006'},
                {'nombre': 'Pollo','id': 'p0007'},
                {'nombre': 'Pescado','id': 'p0008'},
                {'nombre': 'Cordero','id': 'p0009'},
            ]
        },
        {
            'fyv': [
                {'nombre': 'Manzanas','id': 'p0010'},
                {'nombre': 'Peras','id': 'p0011'}
            ]
        }
    ]
    return render(request, 'productos/index.html',{'categorias': categorias, 'productos': productos })