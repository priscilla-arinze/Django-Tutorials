from django.db import models
from django.contrib.auth.models import User # allows user login storage/functionality


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # allows nulls in database and allows user to submit blanks in form
    #participants = 
    updated = models.DateTimeField(auto_now=True) # current date & time of each time a record is updated
    created = models.DateTimeField(auto_now_add=True) # current date & time of only when a record is created

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.name


# One to many relationship model (one user, multiple messages)
class Message(models.Model):
    # on_delete: if a room is deleted, all of the users (children) within the room (parent) will also be deleted (cascading effect)
        # NOTE: User is part of the Django User import (see above)
        # NOTE: the actual user objects are not being deleted, only the references
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # MESSAGES
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField() # actuall message content
    updated = models.DateTimeField(auto_now=True) # current date & time of each time a record is updated
    created = models.DateTimeField(auto_now_add=True) # current date & time of only when a record is created

    def __str__(self):
        return self.body[0:50] # only return the first 50 characters