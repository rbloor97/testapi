from django.urls import path,include
from rest_framework import routers

from api import views
from .views import *

app_name = 'api'
router=routers.DefaultRouter()
     # path('despacho/', DespachoList.as_view()),
router.register(r'producto', views.ProductoList),
router.register(r'factura', views.Factura_ventaList),
router.register(r'proovedor', views.ProovedorList),
router.register(r'categoria', views.CategoriaList),
router.register(r'perchero', views.UserPercheroList),
router.register(r'entrada', views.EntradaList),
router.register(r'ubicacion', views.UbicationList),
router.register(r'perchado', views.PerchadoList),
router.register(r'salida', views.SalidaList)


urlpatterns = [
    path('', include(router.urls)),
]

