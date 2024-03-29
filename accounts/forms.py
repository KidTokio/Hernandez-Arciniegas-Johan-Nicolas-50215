from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class SignUpForm(UserCreationForm):
    
    # Campos personalizados para el formulario de registro
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Formulario de inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Formulario para ajustes de usuario
class UserSettingsForm(forms.ModelForm):
    # Campos personalizados para el formulario de ajustes
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(max_length=254)
    current_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput, required=False)
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["username", "email"]

    # Método para validar los campos
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get("current_password")
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 or new_password2:
            if not current_password:
                raise forms.ValidationError("Debes ingresar tu contraseña actual para cambiarla.")
            if not self.instance.check_password(current_password):
                raise forms.ValidationError("La contraseña actual es incorrecta.")

            if new_password1 != new_password2:
                raise forms.ValidationError("Las nuevas contraseñas no coinciden.")
        
        return cleaned_data

    # Método para guardar los cambios
    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password1")
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user

# Formulario para el avatar de usuario
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
