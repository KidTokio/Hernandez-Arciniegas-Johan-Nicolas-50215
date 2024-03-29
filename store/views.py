from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView
from .forms import GameJamForm, EtiquetaForm, DesarrolladorForm, JuegoForm
from .models import *
from django.urls import reverse_lazy

# NAVEGACION ______________________________________________________________

def index(request):
    juegos = Juego.objects.all()
    return render(request, "store/index.html", {"juegos": juegos})


def about(request):
    return render(request, "store/about.html")


def terminos(request):
    return render(request, "store/terminos.html")


def explorarJuegos(request):
    juegos = Juego.objects.all()
    return render(request, "store/explorarJuegos.html", {"juegos": juegos})


def gameJams(request):
    gameJams = GameJam.objects.all()
    return render(request, "store/gameJams.html", {"gameJams": gameJams})


def detalleJuego(request, id):
    juego = get_object_or_404(Juego, pk=id)
    return render(request, "store/detalleJuego.html", {"juego": juego})


def buscarJuego(request):
    if "buscar" in request.GET and request.GET["buscar"]:
        patron = request.GET["buscar"]
        juegos = Juego.objects.filter(titulo__icontains=patron)
        contexto = {"juegos": juegos}
        return render(request, "store/explorarJuegos.html", contexto)
    
    contexto = {"juegos": Juego.objects.all()}
    return render(request, "store/explorarJuegos.html", contexto)


# CRUD GAMEJAMS ___________________________________________________________

def crearJam(request):
    if request.method == "POST":
        form = GameJamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gamejam")
    else:
        form = GameJamForm()
    return render(request, "store/crearJam.html", {"form": form})


class editarJam(UpdateView):
    model = GameJam
    form_class = GameJamForm
    template_name = "store/editarJam.html"  
    success_url = "/gamejams/"


class borrarJam(DeleteView):
    model = GameJam
    template_name = "store/borrarJam.html" 
    success_url = reverse_lazy("gamejam")


# CRUD JUEGO ___________________________________________________________

# Formularios de juego, etiquetas, y desarrolladores - 1 Sola pagina
    
def subir(request):
    juego_form = JuegoForm()  
    etiqueta_form = EtiquetaForm()  
    desarrollador_form = DesarrolladorForm()  

    etiquetas = Etiqueta.objects.all()
    desarroladores = Desarrollador.objects.all()

    if request.method == "POST":
        if "juego_submit" in request.POST:
            juego_form = JuegoForm(request.POST, request.FILES)  
            if juego_form.is_valid():
                juego = juego_form.save()  

        elif "etiqueta_submit" in request.POST:
            etiqueta_form = EtiquetaForm(request.POST)  
            if etiqueta_form.is_valid():
                etiqueta_form.save()

        elif "desarrollador_submit" in request.POST:
            desarrollador_form = DesarrolladorForm(request.POST)  
            if desarrollador_form.is_valid():
                desarrollador_form.save()

    return render(request, "store/subir.html", {
        "juego_form": juego_form,
        "etiqueta_form": etiqueta_form,
        "desarrollador_form": desarrollador_form,
        "etiquetas": etiquetas,
        "desarrolladores": desarroladores,
    })


class editarJuego(UpdateView):
    model = Juego
    form_class = JuegoForm
    template_name = "store/editarJuego.html"  
    success_url = "/explorar/"


class borrarJuego(DeleteView):
    model = Juego
    template_name = "store/borrarJuego.html" 
    success_url = reverse_lazy("explorar") 


# CRUD ETIQUETAS _________________________________________________________
    
class editarTag(UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = "store/editarTag.html"  
    success_url = "/subir/"


class borrarTag(DeleteView):
    model = Etiqueta
    template_name = "store/borrarTag.html" 
    success_url = reverse_lazy("subirJuego")


# CRUD DESARROLLADORES ___________________________________________________

class editarDev(UpdateView):
    model = Desarrollador
    form_class = DesarrolladorForm
    template_name = "store/editarDev.html"  
    success_url = "/subir/"


class borrarDev(DeleteView):
    model = Desarrollador
    template_name = "store/borrarDev.html" 
    success_url = reverse_lazy("subirJuego") 



def mi_vista(request):
    usuarioActual = request.user
    return render(request, "mi_template.html", {"usuarioActual": usuarioActual})


# VISTA ERROR 404 _______________________________________________________

def error404(request, exception):
    return render(request, "error.html", status=404)
