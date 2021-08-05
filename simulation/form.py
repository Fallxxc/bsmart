from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

    error_messages = {
        'duplicate_username': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }    
    CHOICES = (
        ('Ton Status','Ton Status'),
        ('Professionnel', 'Professionnel'),
        ('Etudiant', 'Etudiant'),
        ('Administrateur', 'Administrateur'),
    )
    status = forms.ChoiceField(choices = CHOICES)

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = user.username
    #     user.save()