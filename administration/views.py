from django.shortcuts import render

# Create your views here.

ad = 'administration'


def home(request):
    return render(request, f'{ad}/home.html')
