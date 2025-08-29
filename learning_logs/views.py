from django.shortcuts import render, redirect   # import redirect(), to redirect user back to topics page after submitting the topic
from .models import Topic      # import model associated with data we need
from .forms import TopicForm   # import the form


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
    
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted. Create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid(): # check all required fields have been filled in, text < 200 characters, etc
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form. Run only in these 2 circumstances
    context = {'form_key': form}
    return render(request, 'learning_logs/new_topic.html', context)




