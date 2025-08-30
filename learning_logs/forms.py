from django import forms    # import the module to build forms

from .models import Topic, Entry   # import model you need

class TopicForm(forms.ModelForm):
    """Build a form automatically with ModelForm"""
    class Meta:
        model = Topic
        fields = ['text']       # include only text, not date
        labels = {'text': ''}   # blank label for text field

class EntryForm(forms.ModelForm):
    """Create a form associated with an entry of a topic"""
    class Meta:
        model = Entry           # based the class on Entry
        fields = ['text']       
        labels = {'text': ''}   # give a blank label to text
        widgets = {'text':forms.Textarea(attrs={'cols':80})}    # override  the default multiline text area with width of 80 columns instead of 40
        