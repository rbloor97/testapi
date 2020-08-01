from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from api.models import *
from .serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import *
from rest_auth.views import LoginView
from rest_framework import generics, viewsets


# class UserRecordView(APIView):
#
#     permission_classes = [IsAdminUser]
#
#     def get(self, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             {
#                 "error": True,
#                 "error_msg": serializer.error_messages,
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )

class UserListView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'Nombre': user.first_name,
            'Apellido': user.last_name,
            'email': user.email
        })

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = Producto_Serializer

class Factura_ventaList(generics.ListCreateAPIView):
    queryset = Factura_venta.objects.all()
    serializer_class = Factura_venta_serializer

class ProovedorList(generics.ListCreateAPIView):
    queryset = Proovedor.objects.all()
    serializer_class = Proovedor_serializer


class ExistenciaList(generics.ListCreateAPIView):
    queryset = Existencia.objects.all()
    serializer_class = Existencia_serializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = Categoria_serializer

class UserPercheroList(generics.ListCreateAPIView):
    queryset = UserPerchero.objects.all()
    serializer_class = UserPerchero_serializer





# class Recibo_pList(generics.ListCreateAPIView):
#     queryset = Recibo_p.objects.all()
#     serializer_class = Recibo_p_Serializer
#
#
# class DespachoList(generics.ListCreateAPIView):
#     queryset = Despacho.objects.all()
#     serializer_class = Despacho_Serializer
