from django.shortcuts import render
from . import forms

# Create your views here.

def home(request):
    cont = {}
    return render(request,'home/home.html',cont)

def edit_profile(request):
    cont = {'form':forms.EditProfileForm}
    return render(request,'home/edit_profile.html',cont)
