from django.shortcuts import render, redirect   # import redirect(), to redirect user back to topics page after submitting the topic
from .models import Topic,  Entry           # import model associated with data we need
from .forms import TopicForm, EntryForm     # import the form for topic and entry


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')  # render the response based on data provided by views

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

def new_entry(request, topic_id):   # store the topic_id from the URL request
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted. Create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)  # make an instance populated with POST data from the request object
        if form.is_valid():                  # check all required fields have been filled
            new_entry = form.save(commit = False)  # do not save to db yet, but wait to add topic
            new_entry.topic = topic
            new_entry.save()                 # save entry to db
            return redirect('learning_logs:topic', topic_id = topic_id) # redirect to the view of all entries of the topic
    
    # Display a blank or invalid form in case info is missing
    context = {'topic_key': topic, 'form_key': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)  # get the entry object that user wants to edit
    topic = entry.topic                     # get the topic

    if request.method != 'POST':
        # Initial request: return pre-fill form with current entry'
        form = EntryForm(instance=entry)    # create the form with the info of the pre-existing entry object
    else:
        # POST changed data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()     # no need to add arguments, because entry is already associated with topic
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = {'entry_key': entry, 'topic_key': topic, 'form_key': form}
    return render(request, 'learning_logs/edit_entry.html', context)






