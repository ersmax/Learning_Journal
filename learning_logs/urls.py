"""Defines URL patterns for learning logs."""
from django.urls import path    # function to build URL paths and map URLs to views
from . import views             # view retrieves and process data, and renders a page

app_name = 'learning_logs'      # helps Django to distinguish this urls.py from files of the same name in other apps
urlpatterns = [                 # list of individual pages that can be requested from the learning_log apps
    # Home page
    path('', views.index, name='index'),# '': base URL (http://localhost:8000). route the request to a view
                                        # views.index: specifies which function to call
                                        # name = 'index': provides the name index for this URL
    # Page with list of topics
    path('topics/', views.topics, name='topics'),       # refer to this URL with the alias 'topics'
    # Page listing all entries of a topic
    path('topics/<int:topic_id>', views.topic, name='topic'), # topic_id is a reference to topic.id 
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for addiging a new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),    # we need a topid_id argument to tell which topic is associated with the entry
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]



