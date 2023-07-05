from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]
