from django.shortcuts import redirect, render
from .models import Carrito, CarritoItem
from tienda.models import Producto

def agregar_carrito(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    producto = Producto.objects.get(id=id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    item, created = CarritoItem.objects.get_or_create(
        carrito=carrito,
        producto=producto
    )

    if not created:
        item.cantidad += 1
        item.save()

    return redirect('ver_carrito')

def ver_carrito(request):
    if not request.user.is_authenticated:
        return redirect('login')

    carrito = Carrito.objects.filter(usuario=request.user).first()
    items = carrito.items.all() if carrito else []

    return render(request, 'carrito/carrito.html', {
        'items': items
    })
