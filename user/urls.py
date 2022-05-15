
from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth
 
urlpatterns = [
    path('', index, name ='index'),
    path('login/', Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/',register, name ='register'),  
    path('activate<uidb64>/<token>/', activate, name='activate'),  
]