from django.db import models


# Etiquetas ligadas a los juegos
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# Modelo de desarrolladores
class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    link = models.URLField()

    def __str__(self):
        return self.nombre


# Modelo de juegos
class Juego(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    lanzamiento = models.DateField()
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/portadas/", default="arcadiaCover.png")
    trailer = models.FileField(upload_to="media/videos/")

    def __str__(self):
        return self.titulo


# Modelo gamejams
class GameJam(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="media/portadas/", default="arcadiaCover.png")
    descripcion = models.TextField()
    premio = models.TextField()
    fechaLimite = models.DateField()

    def __str__(self):
        return self.titulo