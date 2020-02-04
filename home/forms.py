from django import forms
from home.models import Post 

class HomeForm(forms.ModelForm):
    '''
    Form for the home page, with text box for the user
    to post a status, similar to Facebook's timeline 
    '''
    post = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'What\'s on your mind?'
        }
    ))

    class Meta:
        model = Post 
        fields = ('post',)