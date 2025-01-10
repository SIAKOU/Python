# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Adresse(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    num_rue = models.IntegerField(verbose_name="Numéro de la rue")  # Street number
    nom_rue = models.CharField(max_length=100, verbose_name="Nom de la rue")  # Street name
    img_client = models.ImageField(upload_to='images/', verbose_name="Image du client")  # Client image
    ville = models.CharField(max_length=100, verbose_name="Ville")  # City
    pays = models.CharField(max_length=100, verbose_name="Pays")  # Country
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.num_rue} {self.nom_rue}, {self.ville}, {self.pays}"


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, default="Esdeath", verbose_name="Nom")
    prenom = models.CharField(max_length=100, default="Hinata", verbose_name="Prénom")
    adresse = models.ForeignKey(
        Adresse,
        on_delete=models.CASCADE,
        related_name="clients",
        verbose_name="Adresse"
    )

    def __str__(self):
        return f"{self.nom} {self.prenom}, {self.adresse}"
