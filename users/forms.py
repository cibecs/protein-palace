from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ProteinPalaceApp.models import UserProfile

class CustomUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].help_text = None  # Remove the default help text
        self.fields['password1'].help_text = None  # Remove the default help text
        self.fields['password2'].help_text = None  # Remove the default help text

        # Customize widget attributes
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})

        # Update widget attributes for username, password1, and password2 fields
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter a password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter a password'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        
        
    def label_from_instance(self, obj):
        label = super().label_from_instance(obj)
        return label.capitalize()  # Capitalize form labels

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widget attributes
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter a username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter a password'})

    def label_from_instance(self, obj):
        label = super().label_from_instance(obj)
        return label.capitalize()
    
class ProfilePictureForm(forms.ModelForm):
    profilePicture = forms.ImageField(
        label='Change profile picture',
        widget=forms.ClearableFileInput(attrs={'class': 'btn ', 'accept': 'image/*'})
    )
    
    class Meta:
        model = UserProfile
        fields = ('profilePicture',)
