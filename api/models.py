from django.db import models
from django.contrib.auth.models import User


class UserPerchero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    isperchero = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name


class Entrada(models.Model):
    Fecha = models.DateField()
    UserPerchero = models.ForeignKey(UserPerchero, on_delete=models.CASCADE, default=0, blank=True, null=True)


class Categoria(models.Model):
    Nombre = models.CharField(max_length=100, blank=True)
    Descripcion = models.CharField(max_length=300, blank=True)
    UnidadesExistencia = models.IntegerField(default=None, blank=True, null=True)


    def __str__(self):
        return self.Nombre





class Proovedor(models.Model):
    Nombre = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.Nombre


class Factura_venta(models.Model):
    Comprador = models.CharField(max_length=30, blank=True)
    Num_factura = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Num_factura


class Producto(models.Model):
    Estado = models.CharField(max_length=10, blank=True)
    Codigo_barra = models.CharField(max_length=30, blank=True)
    Nombre = models.CharField(max_length=100, blank=True)
    Precio = models.CharField(max_length=30, blank=True)
    Proovedor = models.ForeignKey(Proovedor, on_delete=models.CASCADE, default=None, blank=True, null=True)
    factura_venta = models.ForeignKey(Factura_venta, on_delete=models.CASCADE, default=None, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Ubication(models.Model):
    Nombre= models.CharField(max_length=100, blank=True)
    Estado= models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.Nombre


class Perchado(models.Model):
    fecha = models.DateField(default=None)
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE, default = 0,blank=True,null=True)
    UserPerchero = models.ForeignKey(UserPerchero, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Salida(models.Model):
    fecha= models.DateField(default=None)
    UserPerchero = models.ForeignKey(UserPerchero, on_delete=models.CASCADE, default=0, blank=True, null=True)
