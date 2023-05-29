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
def profile(request):
    myDict = {
        "title": "Profile",
    }
    return render(request,'users/profile.html')