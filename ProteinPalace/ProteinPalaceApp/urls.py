from django.urls import path
from . import views 
urlpatterns = [
	path('', views.mainPage, name = 'mainPage'), 
    path('browse/', views.browse, name = 'browse'),
    path('myrecipes/', views.myrecipes, name = 'myrecipes'),
    path('create/', views.create, name = 'create'),
    path('favorites/', views.favorites, name = 'favorites'),
    path('myaccount/', views.myaccount, name = 'myaccount'),
]