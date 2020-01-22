from django.urls import reverse
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# The Accounts App's Views
def register(request):
    '''

    '''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/reg_form.html', context)


@login_required
def view_profile(request, pk = None):
    '''

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

    '''
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # Keeps user logged in while changing their password
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user = request.user)
        context = {'form': form}
        return render(request, 'accounts/change_password.html', context)
