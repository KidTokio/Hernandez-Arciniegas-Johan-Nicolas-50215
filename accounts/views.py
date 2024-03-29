from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserSettingsForm, UserProfileForm
from .models import UserProfile

# Vista para el registro de usuarios
def registro(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, "accounts/registro.html", {"form": form})

# Vista para iniciar sesión
def iniciarSesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
    return render(request, "accounts/login.html")

# Vista para cerrar sesión
@login_required
def cerrarSesion(request):
    logout(request)
    return redirect("index")
    
# Vista para la configuración del usuario
@login_required
def config(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=user)

    if request.method == "POST":
        user_form = UserSettingsForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("index")
    else:
        user_form = UserSettingsForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, "accounts/config.html", {"user_form": user_form, "profile_form": profile_form})
