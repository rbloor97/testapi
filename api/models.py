from django.db import models
from django.contrib.auth.models import User

# class Recibo_p(models.Model):
#     Usuario_asignado = models.ForeignKey(User, on_delete=models.CASCADE)
#     Num_Recibo = models.CharField(max_length=200)
#     Proovedor = models.CharField(max_length=200)
#
# class Despacho(models.Model):
#     Usuario_asignado = models.ForeignKey(User, on_delete=models.CASCADE)
#     Num_Recibo = models.CharField(max_length=200)
#     Ubicacion = models.CharField(max_length=200)
#     Factura = models.CharField(max_length=200,blank=True)
#     Cliente = models.CharField(max_length=200)

class Proovedor(models.Model):
    Nombre=models.CharField(max_length=100,blank=True)
    direccion=models.CharField(max_length=30,blank=True)
    telefono = models.CharField(max_length=20,blank=True)


class Producto(models.Model):
    Estado=models.CharField(max_length=10,blank=True)
    Codigo_barra=models.CharField(max_length=30,blank=True)
    Nombre=models.CharField(max_length=100,blank=True)
    Precio=models.CharField(max_length=30,blank=True)
    Proovedor=models.ForeignKey(Proovedor,on_delete=models.CASCADE)



