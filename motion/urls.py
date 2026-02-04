from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tienda.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
]
