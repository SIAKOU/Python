"""
URL configuration for DjangoProjectexposer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoProjectexposer import settings
from Mapping import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('login/', views.create_user),
    path('form/', views.form),
    path('map/', views.map),
    path('client/', views.client,name='list_client'),
    path('client/<int:id_client>/', views.client_details,name='client'),
    path('adresse/<int:id_client>/', views.Adresse_Choice, name='ajouter_adresse'),
    path('client/delete/<int:id_client>/', views.supprimer_client, name='supprimer_client'),
    path('client/modifier/<int:id_client>/', views.modifier_client, name='modifier_client'),
]

if settings.DEBUG:  # Servir les fichiers médias seulement en développement
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
