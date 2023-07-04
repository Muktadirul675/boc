from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decorators.auth_dec import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
 
# Create your views here.

au = 'authentication'

@unauthenticated
def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("home:home")
        else:
            messages.error(request,"Wrong credentials!")
    cont = {}
    return render(request,f'{au}/login.html',cont)

@login_required(login_url="/authentication/login")
def logout_user(request):
    logout(request)
    return redirect("home:home")

@unauthenticated
def register(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = user = authenticate(request,username=username,password=password)
        if user is not None:
            messages.info("Email is already registered")
        else:
            new_user = User.objects.create_user(username=username,password=password)
            new_user.email = username
            new_user.save()
            login(request,new_user)
            return redirect("home:home")
    cont = {}
    return render(request,f'{au}/register.html',cont)

