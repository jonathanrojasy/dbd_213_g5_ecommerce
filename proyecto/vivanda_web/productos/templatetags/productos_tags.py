from django import template

register = template.Library()


@register.inclusion_tag('utils/prod_categorias.html')
def prod_categorias(categorias):
    return {'categorias': categorias}

@register.inclusion_tag('utils/prod_listar.html')
def prod_listar(productos):
    return {'productos': productos}

@register.inclusion_tag('utils/prod_tarjeta.html')
def prod_tarjeta(producto):
    return {'producto': producto}