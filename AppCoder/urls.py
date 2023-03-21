
from django.urls import path
from AppCoder.views import producto, crear_producto, usuario, cliente

urlpatterns = [
    path('productos/', producto, name="AppCoderProductos"),
    path('producto/<nombre>/<precio>', crear_producto),
    path('usuarios/', usuario, name="AppCoderUsuarios"),
    path('clientes/', cliente, name="AppCoderClientes"),
]