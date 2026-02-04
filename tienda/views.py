from django.shortcuts import render
from .models import Categoria, Producto

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
