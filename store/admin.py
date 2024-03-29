from django.contrib import admin
from .models import *

class JuegoAdmin(admin.ModelAdmin):
    filter_horizontal = ('etiquetas',)

# Modelos registrados
admin.site.register(Etiqueta)
admin.site.register(Desarrollador)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(GameJam)
