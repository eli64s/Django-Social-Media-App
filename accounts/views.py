from django.urls import reverse
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required


# The Accounts App's Views
def register(request):
    '''
    This view handles user registration, redirecting the user to the home page
    '''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect(reverse('home:home'))

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/reg_form.html', context)


@login_required
def view_profile(request, pk = None):
    '''
    View that renders a user's profile page
    '''
    # Takes user to the selected friend's profile page
    if pk:
        user = User.objects.get(pk = pk)
    else:
        user = request.user

    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    '''
    View that renders the edit profile page
    '''
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))

    else:
        form = EditProfileForm(instance = request.user)
        context = {'form': form}
        return render(request, 'accounts/edit_profile.html', context)


@login_required
def change_password(request):
    '''
    View that handles user password changes 
    '''
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # Keeps user logged in while changing password
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user = request.user)
        context = {'form': form}
        return render(request, 'accounts/change_password.html', context)
