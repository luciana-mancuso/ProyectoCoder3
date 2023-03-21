
from django.urls import path
from AppCoder.views import productos, usuarios, clientes

urlpatterns = [
    path('productos/', productos),
    path('usuarios/', usuarios),
    path('clientes/', clientes),
]