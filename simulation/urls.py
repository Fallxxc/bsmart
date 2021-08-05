from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registrationPage, name = 'registration'), 
    path('login/',views.loginPage, name = 'login'), 
    path('logout/',views.logoutUser, name = "logout"),

    path('',views.home, name = ""), 

    path('alerte/',views.alerte, name = "alerte"), 
    path('attaque/',views.attaque, name = "attaque"), 

]
