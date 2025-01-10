# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    id_cat = models.AutoField(primary_key=True)
    lib_cat = models.CharField(max_length=500, blank=True, null=True)
    img_cat = models.CharField(max_length=90)
    nom_cat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorie'


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(db_column='nom__client',
                                  max_length=128)
    # Field renamed because it contained more than one '_' in a row.
    prenom_client = models.CharField(db_column='prenom__client',
                                  max_length=128)
    adresse_client = models.CharField(db_column='adresse__client',
                                     max_length=200)
    city_client = models.CharField(db_column='city__client',
                                      max_length=200)
    state_client = models.CharField(db_column='state__client',
                                   max_length=200)
    autreinfo_client = models.CharField(max_length=1021, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'client'

class Detailler(models.Model):
    id_prod = models.CharField(primary_key=True,
                               max_length=5)  # The composite primary key (id_prod, id_fact) found, that is not supported. The first column is selected.
    id_fact = models.ForeignKey('Facture', models.DO_NOTHING, db_column='id_fact')
    qte_det = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detailler'
        unique_together = (('id_prod', 'id_fact'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Facture(models.Model):
    id_fact = models.AutoField(primary_key=True)
    id_four = models.ForeignKey('Fournisseur', models.DO_NOTHING, db_column='id_four', blank=True, null=True)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    date_fact = models.DateField()
    remise_fact = models.IntegerField(blank=True, null=True)
    livraison_fact = models.DateTimeField(blank=True, null=True)
    obserb_fact = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facture'


class Fournisseur(models.Model):
    id_four = models.AutoField(primary_key=True)
    sigle_four = models.CharField(max_length=10)
    lib_four = models.CharField(max_length=255)
    tel_four = models.CharField(max_length=15)
    email_four = models.CharField(max_length=255, blank=True, null=True)
    autreinfo_four = models.CharField(max_length=1021, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fournisseur'


class Produit(models.Model):
    id_prod = models.CharField(primary_key=True, max_length=255)
    id_cat = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_cat')
    lib_prod = models.CharField(max_length=128)
    pu_prod = models.IntegerField()
    info_prod = models.TextField(blank=True, null=True, db_comment='informations supplementaires du produit')
    img_dir = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produit'
