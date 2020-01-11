from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
from home.forms import HomeForm
from home.models import Post, Friend 


# Home app views
#@login_required
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm
        posts = Post.objects.all().order_by('-created') # Orders the post on the home page with latest post on top
        users = User.objects.all().exclude(id = request.user.id) # Does not show logged in user on 'Add Friends'
        friend, created = Friend.objects.get_or_create(current_user = request.user)
        friends = friend.users.all()

        args = {'form': form, 'posts': posts, 'users': users, 'friends': friends}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)          # request.post fills form with data received from post request
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user 
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()                  # Reset to an empty form after submited 
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk = pk) # gives us the user

    # Add or remove a friend
    if operation == 'add':
        Friend.make_friend(request.user, friend)

    elif operation == 'remove':
         Friend.lose_friend(request.user, friend)

    return redirect('home:home')