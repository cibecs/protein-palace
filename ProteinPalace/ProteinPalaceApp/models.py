from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime


# Custom name for uploaded recipe images
def recipe_image_filename(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    dish_name = instance.name.replace(" ", "_").lower()
    extension = os.path.splitext(filename)[1]
    new_filename = f"{dish_name}_{timestamp}{extension}"
    return os.path.join('recipe_images', new_filename)
# Custom name for uploaded profile pictures
def user_profile_picture_filename(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    username = instance.user.username
    extension = os.path.splitext(filename)[1]
    new_filename = f"{username}_{timestamp}{extension}"
    return os.path.join('profile_pictures', new_filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followers', blank=True)
    favouriteRecipes = models.ManyToManyField('Recipe')
    profilePicture = models.ImageField(upload_to=user_profile_picture_filename)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=recipe_image_filename)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    comments = models.ManyToManyField('Comment', blank = True) #we can create a recipe without comments
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    postedAt = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
