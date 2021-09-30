from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registrationPage, name = 'registration'), 
    path('login/',views.loginPage, name = 'login'), 
    path('logout/',views.logoutUser, name = "logout"),

    path('',views.home, name = "home"), 
    
    path('cate/',views.cate, name = "cate"), 
    path('vitess_p/',views.vitess_p, name = "vitess_p"), 
    path('frequence/',views.frequence, name = "frequence"), 
    path('profondeur/',views.profondeur, name = "profondeur"), 
    path('niveauControle/',views.niveauControle, name = "niveauControle"), 
    path('niveauPerte/',views.niveauPerte, name = "niveauPerte"), 
    path('simulation/',views.simulation, name = "simulation"), 
#
    path('Natureinformation/',views.Natureinformation, name = "Natureinformation"), 
    path('Parutioninfo/',views.Parutioninfo, name = "Parutioninfo"),
    path('Perceptsupport/',views.Perceptsupport, name = "Perceptsupport"),
    path('Rebondinfo/',views.Rebondinfo, name = "Rebondinfo"),
    path('simulationattack/',views.simulationattack, name = "simulationattack")




]
