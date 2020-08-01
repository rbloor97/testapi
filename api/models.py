from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    Nombre = models.CharField(max_length=100, blank=True)
    Descripcin = models.CharField(max_length=300, blank=True)

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

