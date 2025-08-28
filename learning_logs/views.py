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
    context = {'topics_key': topics}    # 'topics' = key to pass to the template topics.html
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):       # topic_id is a reference to topic.id. topic_id is passed by path, a function that maps URL paths and views 
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)     
    entries = topic.entry_set.order_by('-date_added')   # reverse lookup <modelname>_set and then order by date_added 
    context = {'topic_key': topic, 'entries_key': entries}
    return render(request, 'learning_logs/topic.html', context)
    


