from django.urls import path
from .views import *

urlpatterns = [

    # Rutas de control y manejo de cuentas
    path("registro/", registro, name="registro"),
    path("login/", iniciarSesion, name="iniciarSesion"),
    path("logout/", cerrarSesion, name="cerrarSesion"),
    path("config/", config, name="config"),
]