from django.urls import path
from . import views

urlpatterns = [
    path('enregistrer/', views.enregister_paiement, name='enregistrer_paiement'),
    path('liste/', views.liste_paiements, name='listePaiements'),
    path('invalides/', views.paiements_invalides, name='paiementsInvalides')
]
