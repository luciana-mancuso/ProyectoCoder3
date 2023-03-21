from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return f"Usuario: {self.nombre} - Apellido: {self.apellido}"
    
class Cliente(Usuario):
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"