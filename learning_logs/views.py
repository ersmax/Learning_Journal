from django.shortcuts import render
from .models import Topic   # import model associated with data we need

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):        # pass the URL request for the webpage
    """Show all available topics"""
    # try to change date_added
    topics = Topic.objects.order_by('date_added')   # QuerySet, a Django object similar to a list of objects that work in the db
    context = {'topics': topics}    # 'topics' = key to pass to the template topics.html
    return render(request, 'learning_logs/topics.html', context)

