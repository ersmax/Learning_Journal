"""
Define URL patterns for accounts
   path() build URLS paths, and map URL to views.
   include() enables default authentication URLs provided by Django (eg. login, logout)
"""
from django.urls import path, include   

app_name = 'accounts'   # distinguish urls.py of this app accounts from other apps
urlpatterns = [         # pages that can be reached from localhost/accounts
    # Include default auth urls.
    
    # include login and logout.
    # When Django reads URL login page request, localhost:8000/accounts/login, 
    # the word accounts tells Django to look in accounts/urls.py 
    # and login tells it to send requests to Django's login view
      
    path('', include('django.contrib.auth.urls')),  

]

