from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    Fecha = models.DateField()

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100, blank=True)
    Descripcion = models.CharField(max_length=300, blank=True)

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100, blank=True)
    Apellido = models.CharField(max_length=300, blank=True)

class UserPerchero(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = None,blank=True,null=True)
    isperchero=models.BooleanField(default=True)

class Existencia(models.Model):
    UnidadesExistencia = models.IntegerField(blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, default = None,blank=True,null=True)

class Proovedor(models.Model):
    Nombre=models.CharField(max_length=100,blank=True)
    direccion=models.CharField(max_length=30,blank=True)
    telefono = models.CharField(max_length=20,blank=True)

class Factura_venta(models.Model):
    Comprador = models.CharField(max_length=30, blank=True)
    Num_factura = models.CharField(max_length=100, blank=True)


class Producto(models.Model):
    Estado=models.CharField(max_length=10,blank=True)
    Codigo_barra=models.CharField(max_length=30,blank=True)
    Nombre=models.CharField(max_length=100,blank=True)
    Precio=models.CharField(max_length=30,blank=True)
    Proovedor=models.ForeignKey(Proovedor,on_delete=models.CASCADE, default = None,blank=True,null=True)
    factura_venta = models.ForeignKey(Factura_venta, on_delete=models.CASCADE, default = None,blank=True,null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, default = None,blank=True,null=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, default = None,blank=True,null=True)

class Ubicacion:
    Nombre: models.CharField(max_length=10,blank=True)
    Estado: models.CharField(max_length=10,blank=True)

class Perchado(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=100,blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, default = None,blank=True,null=True)

class Salida(models.Model):
    fecha: models.DateField()
    usuario: models.ForeignKey(Usuario,on_delete=models.CASCADE, default = None,blank=True,null=True)