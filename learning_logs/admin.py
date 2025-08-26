from django.contrib import admin

# Register your models here.
from .models import Topic, Entry    # look for models.py in the same folder of admin.py: .

admin.site.register(Topic)          # manage the model through the admin site
admin.site.register(Entry)          # register an entry for a topic in the admin site
