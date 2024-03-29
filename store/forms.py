from django import forms
from .models import Juego, GameJam, Etiqueta, Desarrollador

# Formulario para agregar o editar un juego
class JuegoForm(forms.ModelForm):
    etiquetas = forms.ModelMultipleChoiceField(queryset=Etiqueta.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Juego
        fields = ["titulo", "descripcion", "etiquetas", "precio", "lanzamiento", "desarrollador", "imagen", "trailer"]

    def save(self, commit=True):
        instance = super(JuegoForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance


# Formulario para una Game Jam
class GameJamForm(forms.ModelForm):
    class Meta:
        model = GameJam
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(GameJamForm, self).__init__(*args, **kwargs)
        self.fields["fechaLimite"].widget.attrs["class"] = "datepicker"


# Formulario para agregar o editar una etiqueta
class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ["nombre"]


# Formulario para agregar o editar un desarrollador
class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = ["nombre", "link"]
