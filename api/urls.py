from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
     # path('despacho/', DespachoList.as_view()),
        path('producto/', ProductoList.as_view()),
        path('factura/', Factura_ventaList.as_view()),
path('proovedor/', ProovedorList.as_view()),
path('existencia/', ExistenciaList.as_view()),
path('categoria/', CategoriaList.as_view()),
path('perchero/', UserPercheroList.as_view()),
path('entrada/', EntradaList.as_view()),
path('usuario/', UsuarioList.as_view()),
path('ubicacion/', UbicacionList.as_view()),
path('perchado/', PerchadoList.as_view()),
path('salida/', SalidaList.as_view()),


]