from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def home(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(activo=True)
    return render(request, 'tienda/home.html', {
        'categorias': categorias,
        'productos': productos
    })

def categoria_view(request, id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(categoria_id=id, activo=True)
    return render(request, 'tienda/categoria.html', {
        'categorias': categorias,
        'productos': productos
    })

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    return render(request, 'tienda/detalle.html', {
        'producto': producto,
        'categorias': categorias
    })