
from django.contrib import admin
from django.urls import path,include
#added for media
from django.conf import settings
from django.conf.urls.static import static

#used for users app
from users import views as user_views

#used for login and logout
from django.contrib.auth import views as auth_views
from users.forms import CustomUserLoginForm

from ProteinPalaceApp.views import error_404_view

from django.urls import re_path

from django.conf import settings

from django.views.static import serve



#added for 404 error: 
handler404 = error_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("ProteinPalaceApp.urls")),
    #urls for users app
    path('register/',user_views.register,name='register'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
     path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=CustomUserLoginForm,
    ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
#added for media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)