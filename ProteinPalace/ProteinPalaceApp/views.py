from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe, Comment


from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#added for the detail view class
from django.views.generic import DetailView, CreateView, UpdateView

from django.shortcuts import redirect

#added for search
from django.db.models import Q

#added for Create recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeCreateForm

#added for messages
from django.contrib import messages

#added for update recipe
from django.contrib.auth.mixins import UserPassesTestMixin

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

    recipes = Recipe.objects.order_by('-createdAt')  # Order recipes by the 'created_at' field in descending order
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Browse",
        "current_page": "browse",  # Set current_page to 'browse'
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse.html', context=myDict) 

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single-recipe.html'

    def post(self, request, *args, **kwargs):
        recipe = self.get_object()  # Get the recipe object
        user_profile = request.user.userprofile  # Get the user's profile
        if 'favorite' in request.POST:
            user_profile.favouriteRecipes.add(recipe)  # Add recipe to favorites
        elif 'unfavorite' in request.POST:
            user_profile.favouriteRecipes.remove(recipe)  # Remove recipe from favorites
        elif 'follow' in request.POST:
            if request.user != recipe.user:
                user_profile.following.add(recipe.user)  # Follow the recipe's user
            else:
                messages.warning(request, "You can't follow yourself.")
        elif 'unfollow' in request.POST:
            user_profile.following.remove(recipe.user)  # Unfollow the recipe's user
        return redirect('recipe-detail', pk=recipe.pk)
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeCreateForm

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def search(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.filter(
        Q(name__icontains=query) | 
        Q(category__name__icontains=query) | 
        Q(user__userprofile__user__username__icontains=query)
    )
    context = {
        'recipes': recipes,
        'query': query
    }
    return render(request, 'search.html', context)


@login_required
def create_comment(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        content = request.POST.get('content')
        recipe = Recipe.objects.get(id=recipe_id)
        comment = Comment.objects.create(user=request.user, content=content)
        recipe.comments.add(comment)
    return redirect('recipe-detail', pk=recipe_id)

@login_required
def following(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    followed_users = request.user.userprofile.following.all()
    recipes = Recipe.objects.filter(user__in=followed_users).order_by('-createdAt') 

    paginator = Paginator(recipes, max_recipes_per_page)
    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Browse",
        "current_page": "following",  # Set current_page to 'following'
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse-following.html', context=myDict)

@login_required
def myrecipes(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = Recipe.objects.filter(user=request.user).order_by('-createdAt') 
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "myrecipes",
        "current_page": "myrecipes",  
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request,'myrecipes.html', context = myDict)

@login_required
def favorites(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = request.user.userprofile.favouriteRecipes.all().order_by('-createdAt') 
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Favorites",
        "current_page": "favorites",  
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request,'favorites.html', context = myDict)

def error_404_view(request, exception):
    return render(request, '404.html')