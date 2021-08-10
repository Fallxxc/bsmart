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
from django.urls import reverse_lazy, reverse
from django.http import FileResponse, Http404

# Create your views here.
import sys
from simulation.form import  CreateUserForm 
from .models import * 


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

# @login_required(login_url = 'login')    
# @allowed_user(allowed_roles=['admin', 'autres'])
def home(request):#liste les buckets
    return render(request,'accounts/home.html')
def alerte(request): 
    cat= Categorie.objects.all()
    vp= VitessePropagation.objects.all()
    fr= Frequence.objects.all()
    pr= Profondeur.objects.all()
    nc= NiveauControle.objects.all()
    np= NiveauPerte.objects.all()
    func(request)
    context={
        "categorie":cat,
        'vitessePropagation':vp,
        'frequence':fr,
        'profondeur':pr,
        'niveauControle':nc,
        'niveauPerte':np,
    }
    return render(request,'alert.html', context)
    
def cate(request): 
    cat= Categorie.objects.all()
    context={
            "categorie":cat
          }
    return render(request,'cate.html', context)

def vitess_p(request): #1
    vp= VitessePropagation.objects.all()
    if request.method == 'POST':
        var = request.POST.get('categorie')
        global vitess
        def vitess():
            return var    
    context={
        "vitessePropagation":vp }
    return render(request,'vitessepropa.html', context)


def frequence(request): #2
    v = vitess()
    recup = []
    recup.append(v)
    fr= Frequence.objects.all()
    if request.method == 'POST':
        var = request.POST.get('vitessePropagation')
        recup.append(var)
        global freq
        def freq():
            return recup
    context={
        "frequence":fr }
    return render(request,'frequence.html', context)

def profondeur(request):#3
    pro= Profondeur.objects.all()
    pr = freq()
    recup2 = []
    recup2.append(pr)
    if request.method == 'POST':
        var = request.POST.get('frequence')
        recup2.append(var)
        global profond
        def profond():
            return recup2
    context={
        'profondeur':pro,
    }
    return render(request,'profondeur.html', context)

def niveauControle(request):#4
    nic  = profond()
    recup3 = []
    recup3.append(nic)
    nc= NiveauControle.objects.all()
    if request.method == 'POST':
        var = request.POST.get('profondeur')
        recup3.append(var)
        global niveaucon
        def niveaucon():
            return recup3
    context={
        'niveauControle':nc
            }
    return render(request,'nivocontrol.html', context)

def niveauPerte(request):
    nip  = niveaucon()
    recup4 = []
    recup4.append(nip)
    np= NiveauPerte.objects.all()
    if request.method == 'POST':
        var = request.POST.get('niveauControle')
        recup4.append(var)
        global nivopert
        def nivopert():
            return recup4
    context={
        'niveauPerte':np
    }
    return render(request,'nivoperte.html', context)


from collections import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def simulation(request):
    filename = '' 
    sim = nivopert()
    recup5, data = [],[]
    recup5.append(sim)
    if request.method == 'POST':
        nip  = request.POST.get('niveauPerte')
        recup5.append(nip)    
    data= list(flatten(recup5))
    sanit1 = ['Crise ou Catastrophe Sanitaire' , 'Maitrisée' , 'Récurrente', 'Locale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit2 = ['Crise ou Catastrophe Sanitaire' , 'Maitrisée' , 'Récurrente', 'Nationale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit3 = ['Crise ou Catastrophe Sanitaire' , 'Maitrisée' , 'Non récurrente', 'Locale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit4 = ['Crise ou Catastrophe Sanitaire' , 'Maitrisée' , 'Non récurrente', 'Nationale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit5 = ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Récurrente', 'Locale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit6 = ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Récurrente', 'Locale', 'Hors Contrôle' , 'Perte humaine']
    sanit7 = ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Récurrente', 'Nationale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit8 = ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Récurrente', 'Nationale', 'Hors Contrôle' , 'Perte humaine']
    sanit9 = ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Non récurrente', 'Locale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit10= ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Non récurrente', 'Locale', 'Hors Contrôle' , 'Perte humaine']
    sanit11= ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Non récurrente', 'Nationale', 'Sous Contrôle' , 'Pas de perte Humaine']
    sanit12= ['Crise ou Catastrophe Sanitaire' , 'Lente' , 'Non récurrente', 'Nationale', 'Hors Contrôle' , 'Perte humaine']
    sanit13= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Récurrente' , 'Locale' , 'Sous Contrôle', 'Pas de perte Humaine']
    sanit14= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Récurrente' , 'Locale' , 'Hors Contrôle', 'Perte humaine']
    sanit15= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Récurrente' , 'Nationale' , 'Sous Contrôle', 'Pas de perte Humaine']
    sanit16= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Récurrente' , 'Nationale' , 'Hors Contrôle', 'Perte humaine']
    sanit17= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Non récurrente' , 'Locale' , 'Sous Contrôle', 'Pas de perte Humaine']
    sanit18= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Non récurrente' , 'Locale' , 'Hors Contrôle', 'Perte humaine']
    sanit19= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Non récurrente' , 'Nationale' , 'Sous Contrôle', 'Pas de perte Humaine']
    sanit20= ['Crise ou Catastrophe Sanitaire', 'Rapide', 'Non récurrente' , 'Nationale' , 'Hors Contrôle', 'Perte humaine']

    # CATASTROPHE NATURELLE 
    nat1=['Crise ou Catastrophe Naturelle', 'Maitrisée', 'Récurrente', 'Locale' , 'Sous Contrôle', 'Matériel']
    nat2=['Crise ou Catastrophe Naturelle', 'Maitrisée', 'Récurrente', 'Nationale' , 'Sous Contrôle' , 'Matériel']
    nat3=['Crise ou Catastrophe Naturelle', 'Maitrisée', 'Non récurrente' , 'Locale'     , 'Sous Contrôle' , 'Matériel']
    nat4=['Crise ou Catastrophe Naturelle', 'Maitrisée', 'Non récurrente', 'Nationale' , 'Sous Contrôle', 'Matériel']
    nat5=['Crise ou Catastrophe Naturelle', 'Lente', 'Récurrente'    , 'Locale'    , 'Sous Contrôle', 'Matériel']
    nat6=['Crise ou Catastrophe Naturelle', 'Lente', 'Récurrente' , 'Locale' , 'Hors Contrôle' , 'Matériel & Humain']
    nat7=['Crise ou Catastrophe Naturelle', 'Lente', 'Récurrente' , 'Locale' , 'Hors Contrôle' , 'Matériel & Humain']
    nat8=['Crise ou Catastrophe Naturelle', 'Lente', 'Récurrente'     ,'Nationale'  ,'Sous Contrôle' ,'Matériel']
    nat9=['Crise ou Catastrophe Naturelle', 'Lente', 'Récurrente'     ,'Nationale'  ,'Hors Contrôle' ,'Matériel & Humain']
    nat10=['Crise ou Catastrophe Naturelle','Lente', 'Non récurrente' ,'Locale'     ,'Sous Contrôle' ,'Matériel']
    nat11=['Crise ou Catastrophe Naturelle','Lente', 'Non récurrente' ,'Locale'     ,'Hors Contrôle' ,'Matériel & Humain']
    nat12=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Nationale'  ,'Hors Contrôle' ,'Matériel & Humain']
    nat13=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Nationale'  ,'Hors Contrôle' ,'Matériel & Humain']
    nat14=['Crise ou Catastrophe Naturelle','Rapide', 'Récurrente'     ,'Locale'     ,'Hors Contrôle' ,'Matériel & Humain']
    nat15=['Crise ou Catastrophe Naturelle','Rapide', 'Récurrente'     ,'Nationale'  ,'Sous Contrôle' ,'Matériel']
    nat16=['Crise ou Catastrophe Naturelle','Rapide', 'Récurrente'     ,'Nationale'  ,'Hors Contrôle' ,'Matériel & Humain']
    nat17=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Locale'     ,'Sous Contrôle' ,'Matériel']
    nat18=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Locale'     ,'Hors Contrôle' ,'Matériel & Humain']
    nat19=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Nationale'  ,'Sous Contrôle' ,'Matériel']
    nat20=['Crise ou Catastrophe Naturelle','Rapide', 'Non récurrente' ,'Nationale'  ,'Hors Contrôle' ,'Matériel & Humain']
    
    # CATASTROPHE SECURITAIRE
    sec1=['Crise ou Catastrophe Sécuritaire', 'Maitrisée',  'Récurrente', 'Locale', 'Sous contrôle', 'Matériel'] 
    sec2=['Crise ou Catastrophe Sécuritaire', 'Maitrisée', 'Récurrente', 'Nationale', 'Sous contrôle', 'Matériel' ]
    sec3=['Crise ou Catastrophe Sécuritaire', 'Maitrisée', 'Non récurrente', 'Locale', 'Sous contrôle','Matériel' ]
    sec4=['Crise ou Catastrophe Sécuritaire', 'Maitrisée', 'Non récurrente', 'Nationale', 'Sous contrôle', 'Matériel']
    sec5=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Récurrente', 'Locale', 'Sous contrôle', 'Matériel']
    sec6=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Récurrente', 'Locale', 'Hors Contrôle' ,'Matériel & Humain' ]
    sec7=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Récurrente', 'Nationale','Sous contrôle', 'Matériel' ]
    sec8=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Récurrente', 'Nationale', 'Hors Contrôle' ,'Matériel & Humain']
    sec9=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Non récurrente', 'Locale', 'Sous contrôle', 'Matériel']
    sec10=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Non récurrente', 'Locale', 'Hors Contrôle' ,'Matériel & Humain']
    sec11=['Crise ou Catastrophe Sécuritaire', 'Lente', 'Non récurrente','Nationale', 'Sous contrôle', 'Matériel']
    sec12=['Crise ou Catastrophe Sécuritaire', 'Lente',  'Non récurrente','Nationale','Hors Contrôle' ,'Matériel & Humain']
    sec13=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Récurrente', 'Locale', 'Sous contrôle', 'Matériel']
    sec14=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Récurrente', 'Locale','Hors Contrôle' ,'Matériel & Humain' ]
    sec15=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Récurrente','Nationale', 'Sous contrôle', 'Matériel' ]
    sec16=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Récurrente','Nationale','Hors Contrôle' ,'Matériel & Humain' ]
    sec17=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Non récurrente', 'Locale', 'Sous contrôle','Matériel' ]
    sec18=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Non récurrente', 'Locale', 'Hors Contrôle' ,'Matériel & Humain']
    sec19=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Non récurrente', 'Nationale','Sous contrôle','Matériel']
    sec20=['Crise ou Catastrophe Sécuritaire', 'Rapide', 'Non récurrente', 'Nationale','Hors Contrôle' ,'Matériel & Humain']

    # la gestion des catastroph sanitaire 
    if data==sanit1:
        filename = 'SANIT1.pdf'
    elif data==sanit2:
        filename = 'SANIT2.pdf'
    elif data==sanit3:
        filename = 'SANIT3.pdf' 
    elif data==sanit4:
        filename = 'SANIT4.pdf'
    elif data==sanit5:
        filename = 'SANIT5.pdf'  
    elif data==sanit6:
        filename = 'SANIT6.pdf'  
    elif data==sanit7:
        filename = 'SANIT7.pdf'  
    elif data==sanit8:
        filename = 'SANIT8.pdf'  
    elif data==sanit9:
        filename = 'SANIT9.pdf'  
    elif data==sanit10:
        filename = 'SANIT10.pdf'
    elif data==sanit11:
        filename = 'SANIT11.pdf'

    elif data==sanit12:
        filename = 'SANIT12.pdf'

    elif data==sanit13:
        filename = 'SANIT13.pdf'

    elif data==sanit14:
        filename = 'SANIT14.pdf'

    elif data==sanit15:
        filename = 'SANIT15.pdf'

    elif data==sanit16:
        filename = 'SANIT16.pdf'
    
    elif data==sanit17:
        filename = 'SANIT17.pdf' 
        
    elif data==sanit18:
        filename = 'SANIT18.pdf'
    
    elif data==sanit19:
        filename = 'SANIT19.pdf' 
    
    elif data==sanit20:
        filename = 'SANIT20.pdf'

    # gestion des Catastrophe naturelles
    elif data==nat1:
        filename = 'NATUREL1.pdf'
    elif data==nat2:
        filename = 'NATUREL2.pdf'
    elif data==nat3:
        filename = 'NATUREL3.pdf' 
    elif data==nat4:
        filename = 'NATUREL4.pdf'
    elif data==nat5:
        filename = 'NATUREL5.pdf'  
    elif data==nat6:
        filename = 'NATUREL6.pdf'  
    elif data==nat7:
        filename = 'NATUREL7.pdf'  
    elif data==nat8:
        filename = 'NATUREL8.pdf'  
    elif data==nat9:
        filename = 'NATUREL9.pdf'  
    elif data==nat10:
        filename = 'NATUREL10.pdf'
    elif data==nat11:
        filename = 'NATUREL11.pdf'
   
    elif data==nat12:
        filename = 'NATUREL12.pdf'

    elif data==nat13:
        filename = 'NATUREL13.pdf'

    elif data==nat14:
        filename = 'NATUREL14.pdf'

    elif data==nat15:
        filename = 'NATUREL15.pdf'

    elif data==nat16:
        filename = 'NATUREL16.pdf'
    
    elif data==nat17:
        filename = 'NATUREL17.pdf' 
        
    elif data==nat18:
        filename = 'NATUREL18.pdf'
    
    elif data==nat19:
        filename = 'NATUREL19.pdf' 
    
    elif data==nat20:
        filename = 'NATUREL20.pdf'

    # la gestion des Catastrophe securitaire
    elif data==sec1:
        filename = 'SECUR1.pdf'
    elif data==sec2:
        filename = 'SECUR2.pdf'
    elif data==sec3:
        filename = 'SECUR3.pdf' 
    elif data==sec4:
        filename = 'SECUR4.pdf'
    elif data==sec5:
        filename = 'SECUR5.pdf'  
    elif data==sec6:
        filename = 'SECUR6.pdf'  
    elif data==sec7:
        filename = 'SECUR7.pdf'  
    elif data==sec8:
        filename = 'SECUR8.pdf'  
    elif data==sec9:
        filename = 'SECUR9.pdf'  
    elif data==sec10:
        filename = 'SECUR10.pdf'
    elif data==sec11:
        filename = 'SECUR11.pdf'
   
    elif data==sec12:
        filename = 'SECUR12.pdf'

    elif data==sec13:
        filename = 'SECUR13.pdf'

    elif data==sec14:
        filename = 'SECUR14.pdf'

    elif data==sec15:
        filename = 'SECUR15.pdf'

    elif data==sec16:
        filename = 'SECUR16.pdf'
    
    elif data==sec17:
        filename = 'SECUR17.pdf' 
        
    elif data==sec18:
        filename = 'SECUR18.pdf'
    
    elif data==sec19:
        filename = 'SECUR19.pdf' 
    
    elif data==sec20:
        filename = 'SECUR20.pdf'
    else:
        pass
    
    context={
        'recup':data,
        'filename':filename
    }
    return render (request, 'simulation.html', context) 

# @login_required(login_url = 'login')    
# @allowed_user(allowed_roles=['admin', 'autres'])
def attaque(request):#liste les buckets
    return render(request,'attaque.html')
