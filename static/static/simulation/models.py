from django.db import models

# Create your models here.

class Categorie(models.Model):
    cathegorie_name = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.cathegorie_name}"

class VitessePropagation(models.Model):
    vitesse = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.vitesse}"

class Frequence(models.Model):
    frequence = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.frequence}"

class Profondeur(models.Model):
    profondeur = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.profondeur}"

class NiveauControle(models.Model):
    niveau_control = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_control}"

class NiveauPerte(models.Model):
    niveau_perte = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_perte}"


class Niveaualerte(models.Model):
    niveau_alerte = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_alerte}"

# GESTION DES ATTAQUES

class NatureInformation(models.Model):
    natur_info = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.natur_info}"


class Qualification(models.Model):
    qualification = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.qualification}"


class Parution(models.Model):
    espace_parution = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.espace_parution}"

class Perceptionsupport(models.Model):
    credibilite = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.credibilite}"        

class Rebond(models.Model):
    rebond = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.rebond}"



