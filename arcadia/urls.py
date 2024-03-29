from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("store.urls")), # ---- Urls de la tienda
    path("", include("accounts.urls")), # ---- Urls de manejo de usuarios

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "store.views.error404"