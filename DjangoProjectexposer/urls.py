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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Mapping import views as mapping_views
from paiement import views as paiement_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapping_views.Home, name='home'),
    path('login/', mapping_views.create_user),
    path('form/', mapping_views.form, name='form'),
    path('map/', mapping_views.map),
    path('client/', mapping_views.client, name='list_client'),
    path('client/<int:id_client>/', mapping_views.client_details, name='client'),
    path('adresse/<int:id_client>/', mapping_views.Adresse_Choice, name='ajouter_adresse'),
    path('client/delete/<int:id_client>/', mapping_views.supprimer_client, name='supprimer_client'),
    path('client/modifier/<int:id_client>/', mapping_views.modifier_client, name='modifier_client'),

    # URLs pour paiement
    path('paiement/enregistrer/', paiement_views.enregister_paiement, name='enregistrer_paiement'),
    path('paiement/liste/', paiement_views.liste_paiements, name='listePaiements'),
    path('paiement/invalides/', paiement_views.paiements_invalides, name='paiementsInvalides'),
    path('paiement/telecharger_recu/<int:id_paiement>/', paiement_views.telecharger_recu, name='telecharger_recu'),
    path('paiement/delete/<int:id_paiement>/', paiement_views.supprimer_paiement, name='supprimer_paiement'),
    path('api/search-marchandises/', paiement_views.search_marchandises, name='search_marchandises'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
