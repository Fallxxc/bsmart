from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Categorie)
admin.site.register(VitessePropagation)
admin.site.register(Frequence)
admin.site.register(Profondeur)
admin.site.register(NiveauControle)
admin.site.register(NiveauPerte)
admin.site.register(Niveaualerte)