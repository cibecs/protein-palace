from django import forms
from .models import Recipe

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control pb-5 ', 'accept': 'image/*', 'placeholder': 'Image'}),
        }
