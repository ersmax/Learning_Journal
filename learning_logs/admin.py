from django.contrib import admin

# Register your models here.
from .models import Topic, Entry    # import models.py from the same folder of admin.py: .

admin.site.register(Topic)          # manage the model through the admin site
admin.site.register(Entry)          # reigster an entry for a topic in the admin site
