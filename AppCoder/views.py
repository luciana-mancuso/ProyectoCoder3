from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Producto, Usuario, Cliente

# Create your views here.
def productos(request):
    return render(request, "index.html")

def usuarios(request):
    pass

def clientes(request):
    pass
