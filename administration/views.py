from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

ad = 'administration'


def home(request):
    users = User.objects.all()
    cont = {'users':users}
    return render(request, f'{ad}/home.html',cont)
