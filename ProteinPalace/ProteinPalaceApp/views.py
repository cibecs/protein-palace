from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    myDict = {
        "title": "Home",
        "current_page": "home",
    }
    return render(request,'index.html', context=myDict)

def browse(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Browse",
        "current_page": "browse",
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse.html', context=myDict)

@login_required
def following(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    followed_users = request.user.userprofile.following.all()
    recipes = Recipe.objects.filter(user__in=followed_users)

    paginator = Paginator(recipes, max_recipes_per_page)
    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Following",
        "current_page": "following",
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse-following.html', context=myDict)


def myrecipes(request):
    return HttpResponse("My Recipes")

def create(request):
    return HttpResponse("Create")
def favorites(request):
    return HttpResponse("Favorites")
def myaccount(request):
    return HttpResponse("My Account")