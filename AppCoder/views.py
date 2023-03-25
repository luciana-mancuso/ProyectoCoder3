from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Producto, Usuario, Cliente
from AppCoder.forms import ProductoForm
from AppCoder.forms import ClienteForm
from AppCoder.forms import BusquedaUsuarioForm

# Create your views here.

def producto(request):
    if request.method=="POST":
        mi_formulario=ProductoForm(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            producto_save=Producto(nombre=informacion['nombre'], precio=informacion['precio'])
            producto_save.save()
        return redirect("AppCoderClientes")
    
    all_productos=Producto.objects.all()
    context={"productos": all_productos, "form":ProductoForm()}
    return render(request, "AppCoder/productos.html", context=context)

def crear_producto(request, nombre, precio):
    save_producto=Producto(nombre=nombre, precio=int(precio))
    save_producto.save()
    context={"nombre": nombre, "precio":precio}
    return render(request, "AppCoder/save_producto.html", context)

def usuario(request):
    all_usuarios=Usuario.objects.all()
    context={"usuarios": all_usuarios, "form_busqueda":BusquedaUsuarioForm}
    return render(request, "AppCoder/usuarios.html", context=context)

def cliente(request):
    if request.method=="POST":
        mi_formulario=ClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            cliente_save=Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'])
            cliente_save.save()
    all_clientes=Cliente.objects.all()
    context={"clientes": all_clientes, "form":ClienteForm}
    return render(request, "AppCoder/clientes.html", context=context)



def busqueda_usuario(request):
    mi_formulario = BusquedaUsuarioForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        usuarios_filtrados = Usuario.objects.filter(apellido__icontains=informacion['apellido'])
        context = {"usuarios": usuarios_filtrados}
        return render(request, "AppCoder/busqueda_usuario.html", context=context)