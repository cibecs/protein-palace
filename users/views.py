from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

#custom form
from . import forms

#decorator for login required
from django.contrib.auth.decorators import login_required

#to create userProfile
from ProteinPalaceApp.models import UserProfile
from ProteinPalaceApp.models import Recipe

from .forms import ProfilePictureForm

#to get user profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = forms.CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            UserProfile.objects.create(user=user)  # Create a UserProfile for the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You are now able to log in.')
            return redirect('browse')
    else:
        form = forms.CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request, username):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            profile_picture = form.cleaned_data['profilePicture']
            user_profile = request.user.userprofile
            user_profile.profilePicture = profile_picture
            user_profile.save()
            messages.success(request, 'Your profile picture has been updated!')
            return redirect('profile', username=request.user.username)
        elif 'follow' in request.POST:
            user = get_object_or_404(User, username=username)
            if request.user != user:
                request.user.userprofile.following.add(user)
        elif 'unfollow' in request.POST:
            user = get_object_or_404(User, username=username)
            request.user.userprofile.following.remove(user)
    else:
        form = ProfilePictureForm()
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(user=user).order_by('-createdAt')[:3]
    context = {'user': user, 
               'title': user.username,
               'recipes': recipes,
               'form': form
              }
    return render(request, 'users/profile.html', context=context)

