"""Defines URL patterns for learning logs."""
from django.urls import path    # function to build URL paths and map URLs to views
from . import views             # view retrieves and process data, and renders a page

app_name = 'learning_logs'      # helps Django to distinguish this urls.py from files of the same name in other apps
urlpatterns = [                 # list of individual pages that can be requested from the learning_log apps
    # Home page
    path('', views.index, name='index') # '': base URL (http://localhost:8000). route the request to a view
                                        # views.index: specifies which function to call
                                        # name = 'index': provides the name index for this URL
]



