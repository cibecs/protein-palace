from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainPage(request):
    myDict = {
        "title": "Home",
        "current_page": "home",
    }
    return render(request,'index.html')

def browse(request):
    myDict = {
        "title": "Browse",
        "current_page": "browse",
    }
    return render(request,'browse.html', context=myDict)

def myrecipes(request):
    return HttpResponse("My Recipes")

def create(request):
    return HttpResponse("Create")
def favorites(request):
    return HttpResponse("Favorites")
def myaccount(request):
    return HttpResponse("My Account")