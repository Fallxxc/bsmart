from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    CHOICES = (
        ('Professionnel', 'Professionnel'),
        ('Etudiant', 'Etudiant'),
        ('Administrateur', 'Administrateur'),
    )
    fist_name = models.CharField(max_length = 200, blank = True)
    last_name = models.CharField(max_length = 200, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(max_length = 200, blank = True)
    avatar = models.ImageField(default = 'avatar.png', upload_to = 'avatars/')
    statut = models.CharField(max_length = 200, choices = CHOICES)
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"