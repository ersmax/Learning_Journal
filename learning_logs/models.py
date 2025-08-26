from django.db import models

# Create your models here.
class Topic(models.Model):                                  # inherit from Model
    """A topic the user is writing on"""
    text = models.CharField(max_length=200)                 # reserve 200 char in the db to hold names
    date_added = models.DateTimeField(auto_now_add=True)    # when user create a new topic, automatically add data and time

    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """An entry for a topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)    # Topic is the foreign key; when a topic is deleted, all the entries associated with it should be deleted too.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)            # present entries in the order they are created

    class Meta:
        verbose_name_plural = 'entries'                             # without this attribute, Django would refer to multiple entries as Entrys

    def __str__(self):
        """Return a short string representing the entry"""
        if len(self.text) < 80:
            return self.text
        return f"{self.text[:80]}..."