# Generated by Django 5.1.4 on 2025-01-10 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mapping', '0002_adresse_delete_categorie_delete_detailler_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='autreinfo_client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='nom_client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.AddField(
            model_name='client',
            name='adresse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Mapping.adresse'),
        ),
        migrations.AddField(
            model_name='client',
            name='nom',
            field=models.CharField(default='Esdeath', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='prenom',
            field=models.CharField(default='Hinata', max_length=100),
        ),
        migrations.AlterModelTable(
            name='client',
            table=None,
        ),
    ]
