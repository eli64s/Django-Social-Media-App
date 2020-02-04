from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    '''
    User registration with basic fields including a username,
    first and last name, email address, and password 
    '''
    email = forms.EmailField(required = True)

    class Meta: 
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit = True):
        '''
        Saves the user's registered information
        '''
        user = super(RegistrationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    '''
    Form to edit the user profile
    '''
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
