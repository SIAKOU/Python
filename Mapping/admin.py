from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id_client', 'nom_client','prenom_client', 'email', 'autreinfo_client','city_client','adresse_client','state_client')  # Colonnes à afficher dans la liste
    search_fields = ('nom_client', 'email')  # Champs pour la recherche
    list_filter = ('nom_client',)  # Ajouter des filtres si nécessaire

# Enregistrement du modèle dans l'interface d'administration
admin.site.register(Client, ClientAdmin)
