from django.contrib import admin
from django.urls import path
from .views import register,login_,success,home,logout_
urlpatterns = [
    path('',home,name='home'),
    path('login',login_,name='login'),
    path('logout',logout_,name='logout'),
    path('register',register,name='register'),
    path('success',success,name='success'),
]