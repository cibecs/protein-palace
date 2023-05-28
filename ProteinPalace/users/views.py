from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

#custom form
from . import forms

def login(request):
    return render(request,'users/login.html')


def register(request):
    if request.method == 'POST':
        form = forms.CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You are now able to log in.')
            return redirect('browse')
    else:
        form = forms.CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)



def profile(request):
    return render(request,'users/profile.html')