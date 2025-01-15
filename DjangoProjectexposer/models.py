from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, default="joan")
    prenom = models.CharField(max_length=100, default="hinata")
    img_client = models.ImageField(upload_to='images/', verbose_name="Image du client",
                                   default="jooan.jpg")  # Client image
    email = models.EmailField(max_length=200, unique=True, default="arise@gmail.com")


class Adresse(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    id_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="adresse",
    )
    num_rue = models.IntegerField(verbose_name="Numéro de la rue")  # Street number
    nom_rue = models.CharField(max_length=100, verbose_name="Nom de la rue")  # Street name
    city = models.CharField(max_length=100, verbose_name="Ville")  # City
    state = models.CharField(max_length=100, verbose_name="Pays")  # Country
    latitude = models.FloatField()
    longitude = models.FloatField()


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
