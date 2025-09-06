"""
Define URL patterns for accounts
   path() build URLS paths, and map URL to views.
   include() enables default authentication URLs provided by Django (eg. login, logout)
"""
from django.urls import path, include 
from . import views  

app_name = 'accounts'   # distinguish urls.py of this app accounts from other apps
urlpatterns = [         # pages that can be reached from localhost/accounts
    
    
    # When Django reads URL login page request, localhost:8000/accounts/login, 
    # the word accounts tells Django to look in accounts/urls.py 
    # and login tells Django to send requests to Django's default login view

    # Include default auth urls, including login & logout
    path('', include('django.contrib.auth.urls')),  
    # Registration page
    path('register/', views.register, name="register"),

]

