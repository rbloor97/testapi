from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
     # path('despacho/', DespachoList.as_view()),
        path('producto/', ProductoList.as_view()),
        # path('recibo/', Recibo_pList.as_view()),

    # path('listuser/', CustomLoginView.as_view(), name='my_custom_login'),
]