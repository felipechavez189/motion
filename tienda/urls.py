from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:id>/', views.categoria_view, name='categoria'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),

]
