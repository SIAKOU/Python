# Generated by Django 5.1.4 on 2025-01-10 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mapping', '0003_remove_client_autreinfo_client_remove_client_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresse',
            name='img_client',
            field=models.ImageField(upload_to='images/', verbose_name='Image du client'),
        ),
        migrations.AlterField(
            model_name='adresse',
            name='nom_rue',
            field=models.CharField(max_length=100, verbose_name='Nom de la rue'),
        ),
        migrations.AlterField(
            model_name='adresse',
            name='num_rue',
            field=models.IntegerField(verbose_name='Numéro de la rue'),
        ),
        migrations.AlterField(
            model_name='adresse',
            name='pays',
            field=models.CharField(max_length=100, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='adresse',
            name='ville',
            field=models.CharField(max_length=100, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='client',
            name='adresse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='Mapping.adresse', verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(default='Esdeath', max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(default='Hinata', max_length=100, verbose_name='Prénom'),
        ),
    ]
