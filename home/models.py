from django.db import models
from django.contrib.auth.models import User

# The Home App's Models
class Post(models.Model):
    '''
    User can post a message in their newsfeed on the homepage timeline, with
    text under the post displaying the user who posted and the time of it
    '''
    post = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True) # Allows user to edit post in the future
    

class Friend(models.Model):
    '''
    Many-to-Many model used for adding and removing other users on the site
    '''
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name = 'owner', null = True, on_delete = models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        '''
        Function to add a user to your friends list
        '''
        friend, created = cls.objects.get_or_create(current_user = current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        '''
        Function to remove a user from your firends lists
        '''
        friend, created = cls.objects.get_or_create(current_user = current_user)
        friend.users.remove(new_friend)