from django.urls import path
from . import views 


urlpatterns = [
	path('', views.home, name = 'home'), 
    path('browse/', views.browse, name = 'browse'),
    path('myrecipes/', views.myrecipes, name = 'myrecipes'),
    path('favorites/', views.favorites, name = 'favorites'),
    path('following/', views.following, name = 'following'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(template_name = "single-recipe.html"), name = 'recipe-detail'),
    path('recipe/comment/create/', views.create_comment, name='comment-create'), 
    path('search/', views.search, name='search'), 
    path('recipe/create/', views.RecipeCreateView.as_view(template_name = "create.html"), name = 'recipe-create'),
]