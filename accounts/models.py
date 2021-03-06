from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# The Accounts App's Models
#class UserProfileManager(models.Manager):
#    '''

#    '''
#    def get_queryset(self):
#    return super(UserProfileManager, self).get_queryset().filter(last_name = 'Salamie')


class UserProfile(models.Model): 	
    '''
    User profile model including username, first and last name,
    email address, and a profile picture displayed on the profile page
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField( max_length = 25)
    email = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'profile_image', blank = True)

    #salamie = UserProfileManager()
    #objects = models.Manager()
    
    def __str__(self):
        return self.user.username
    

def create_profile(sender, **kwargs):
    '''
    Function that creates the user profile 
    '''
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)