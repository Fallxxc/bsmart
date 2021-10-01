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
# from buckets.form import BucketForm, CreateUserForm 
# from buckets.decorators import unauthenticated_user, allowed_user, admin_only



# # @unauthenticated_user
# def registrationPage(request):
# 	form = CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, 'Account was created for ' + username)
# 			return redirect('login')
# 	context = {'form':form}
# 	return render(request, 'templates/accounts/registration.html', context)

# # @unauthenticated_user
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('')
#         else:
#             messages.info(request,'Username or password is incorrect')
#     context = {}            
#     return render(request,'templates/accounts/login.html')  

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')
