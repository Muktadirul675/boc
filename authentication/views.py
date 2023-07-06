from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decorators.auth_dec import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from boc import settings
import random 
 
# Create your views here.

au = 'authentication'

def set_username(first_name):
    total_users = User.objects.all().count()
    relaive_number = int(total_users/100)
    id_range_start = relaive_number * 100 
    id_range_end = ((relaive_number+1) * 100) - 1
    id =  random.randint(id_range_start,id_range_end)
    username = f"{first_name}{id}"
    while(True):
        if User.objects.filter(username = username).exists():
            id =  random.randint(id_range_start,id_range_end)
            username = f"{first_name}{id}"
            print("Getting a new username")
            continue
        else:
            break
    return username

@unauthenticated
def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user = authenticate(request,username=user.username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in")
                return redirect("home:home")
            else:
                messages.error(request,"Invalid Password")
        else:
            messages.error("Email is not registered")
    cont = {}
    return render(request,f'{au}/login.html',cont)

@login_required(login_url="/authentication/login")
def logout_user(request):
    logout(request)
    return redirect("home:home")

@unauthenticated
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        username = set_username(first_name)
        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email is already registered")
        elif password != cpassword:
            messages.error(request,"Password didn't match")
        else:
            new_user = User.objects.create_user(username=username,email=email,password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,f"Successfully Signed in as {username}!")
            
            return redirect("home:home")
    cont = {}
    return render(request,f'{au}/register.html',cont)

