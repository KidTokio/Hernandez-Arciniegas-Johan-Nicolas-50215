from django.urls import path
from .views import *

urlpatterns = [
    # NAVEGACION PRINCIPAL
    path("", index, name="index"), # Pagina principal
    path("sobremi/", about, name="sobremi"), # About
    path("explorar/", explorarJuegos, name="explorar"), # Explorar juegos
    path("gamejams/", gameJams, name="gamejam"), # Explorar gamejams
    path('juego/<int:id>/', detalleJuego, name='detalleJuego'), # Pagina de cada juego
    path("buscar/", buscarJuego, name="buscarJuego"), # Pagina de busqueda/resultados
    path("tym/", terminos, name="terminos"), # Pagina de terminos y condiciones

    # RUTAS CRUD JUEGOS
    path("subir/", subir, name="subirJuego"), # Formularios de juego, etiquetas, y desarrolladores - 1 Sola pagina
    path('editarjuego/<int:pk>/', editarJuego.as_view(), name="editarJuego"),
    path('borrarjuego/<int:pk>/', borrarJuego.as_view(), name='borrarJuego'),

    # RUTAS CRUD GAMEJAM
    path("crearjam/", crearJam, name="crearJam"),
    path('editarjam/<int:pk>/', editarJam.as_view(), name="editarJam"),
    path('borrarjam/<int:pk>/', borrarJam.as_view(), name='borrarJam'),

    # RUTAS CRUD ETIQUETAS ||
    path('editartag/<int:pk>/', editarTag.as_view(), name="editarTag"),
    path('borrartag/<int:pk>/', borrarTag.as_view(), name='borrarTag'),

    # RUTAS CRUD DESARROLLADOR ||
    path('editardev/<int:pk>/', editarDev.as_view(), name="editarDev"),
    path('borrardev/<int:pk>/', borrarDev.as_view(), name='borrarDev'),
]
