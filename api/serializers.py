from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Producto


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

# class Recibo_p_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Recibo_p
#         fields=("__all__")

class Producto_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields=("__all__")

# class Despacho_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Despacho
#         fields=("__all__")
