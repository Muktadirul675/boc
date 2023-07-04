from django.shortcuts import render, redirect
from django.http import HttpResponse
import time
from .tasks import *

# Create your views here.

def home(request):
    # time.sleep(20)
    handle_sleep.delay()
    return HttpResponse("Hello from celery")

def mail(request):
    send_email_func.delay()
    return HttpResponse("Sent email")
