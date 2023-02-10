from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.advisor_signup, name='signup'),
    path('profile/', views.advisor_profile, name='profile'),

]
