from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Producto, Usuario, Cliente

# Create your views here.

def producto(request):
    all_productos=Producto.objects.all()
    context={"productos": all_productos}
    return render(request, "AppCoder/productos.html", context=context)

def crear_producto(request, nombre, precio):
    save_producto=Producto(nombre=nombre, precio=int(precio))
    save_producto.save()
    context={"nombre": nombre, "precio":precio}
    return render(request, "AppCoder/save_producto.html", context)

def usuario(request):
    all_usuarios=Usuario.objects.all()
    context={"usuarios": all_usuarios}
    return render(request, "AppCoder/usuarios.html", context=context)

def cliente(request):
    all_clientes=Cliente.objects.all()
    context={"clientes": all_clientes}
    return render(request, "AppCoder/clientes.html", context=context)
