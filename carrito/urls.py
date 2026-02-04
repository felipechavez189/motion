from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:id>/', views.agregar_carrito, name='agregar_carrito'),
    path('', views.ver_carrito, name='ver_carrito'),
]
