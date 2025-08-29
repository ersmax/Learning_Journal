from django import forms    # import the module to build forms

from .models import Topic   # import model you need

class TopicForm(forms.ModelForm):
    """Build a form automatically with ModelForm"""
    class Meta:
        model = Topic
        fields = ['text']       # include only text, not date
        labels = {'text': ''}

