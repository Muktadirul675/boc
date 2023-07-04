from django.shortcuts import render

# Create your views here.

def home(request):
    cont = {}
    return render(request,'home/home.html',cont)
