from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import *


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class Producto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ("__all__")


class UserPerchero_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserPerchero
        fields = ("__all__")


class Categoria_serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("__all__")


class Existencia_serializer(serializers.ModelSerializer):
    class Meta:
        model = Existencia
        field = ("__all__")


class Proovedor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Proovedor
        field = ("__all__")


class Factura_venta_serializer(serializers.ModelSerializer):
    class Meta:
        model = Factura_venta
        field = ("__all__")


class Entrada_serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        field = ("__all__")


class Ubication_serializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        field = ("__all__")


class Perchado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Perchado
        field = ("__all__")


class Salida_serializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        field = ("__all__")

# class Despacho_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Despacho
#         fields=("__all__")
