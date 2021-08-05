from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
import sys
from simulation.form import  CreateUserForm 
from .models import * 


# @login_required(login_url = 'login')    
# @allowed_user(allowed_roles=['admin', 'autres'])
def home(request):#liste les buckets
    return render(request,'accounts/home.html')


# @login_required(login_url = 'login')    
# @allowed_user(allowed_roles=['admin', 'autres'])
def alerte(request):
    categorie = request.POST.get('categorie')
    vitessePropagation = request.POST.get('vitessePropagation')
    frequence= request.POST.get('frequence')
    profondeur= request.POST.get('profondeur')
    niveauControle=request.POST.get('niveauControle')
    niveauPerte = request.POST.get('niveauPerte')
    niveaualerte   = request.POST.get('niveaualerte')

    print(categorie, vitessePropagation,frequence,profondeur,niveauControle,niveauPerte,niveaualerte)

    categorie= Categorie.objects.all()
    vitessePropagation= VitessePropagation.objects.all()
    frequence= Frequence.objects.all()
    profondeur= Profondeur.objects.all()
    niveauControle= NiveauControle.objects.all()
    niveauPerte= NiveauPerte.objects.all()
    niveaualerte= Niveaualerte.objects.all()
    context={
        "categorie":categorie,
        'vitessePropagation':vitessePropagation,
        'frequence':frequence,
        'profondeur':profondeur,
        'niveauControle':niveauControle,
        'niveauPerte':niveauPerte,
        'niveaualerte':niveaualerte,
    }
    return render(request,'alert.html', context)

# @login_required(login_url = 'login')    
# @allowed_user(allowed_roles=['admin', 'autres'])
def attaque(request):#liste les buckets
    categorie = request.POST.get('categorie')
    vitessePropagation = request.POST.get('vitessePropagation')
    frequence= request.POST.get('frequence')
    profondeur= request.POST.get('profondeur')
    niveauControle=request.POST.get('niveauControle')
    niveauPerte = request.POST.get('niveauPerte')
    niveaualerte   = request.POST.get('niveaualerte')

    print(categorie, vitessePropagation,frequence,profondeur,niveauControle,niveauPerte,niveaualerte)

    categorie= Categorie.objects.all()
    vitessePropagation= VitessePropagation.objects.all()
    frequence= Frequence.objects.all()
    profondeur= Profondeur.objects.all()
    niveauControle= NiveauControle.objects.all()
    niveauPerte= NiveauPerte.objects.all()
    niveaualerte= Niveaualerte.objects.all()
    context={
        "categorie":categorie,
        'vitessePropagation':vitessePropagation,
        'frequence':frequence,
        'profondeur':profondeur,
        'niveauControle':niveauControle,
        'niveauPerte':niveauPerte,
        'niveaualerte':niveaualerte,
        }   
    return render(request,'attaque.html', context)

    #  categorie= Categorie.objects.all()
#     vitessePropagation= VitessePropagation.objects.all()
#     frequence= Frequence.objects.all()
#     profondeur= Profondeur.objects.all()
#     niveauControle= NiveauControle.objects.all()
#     niveauPerte= NiveauPerte.objects.all()
#     niveaualerte= Niveaualerte.objects.all()
#     context={
#         'categorie':categorie,
        # 'vitessePropagation':vitessePropagation,
        # 'frequence':frequence,
        # 'profondeur':profondeur,
        # 'NiveauPerte':NiveauPerte,
        # 'NiveauPerte':NiveauPerte,
        # 'Niveaualerte':Niveaualerte,
    # }


# @unauthenticated_user
def registrationPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'accounts/registration.html', context)

# @unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request,'Username or password is incorrect')
    context = {}            
    return render(request,'accounts/login.html')  

def logoutUser(request):
	logout(request)
	return redirect('login')
