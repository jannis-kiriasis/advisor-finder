from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.seeker_signup, name='seeker_signup'),
    path('profile/', views.seeker_profile, name='seeker_profile'),
    path('delete/', views.delete_profile, name='seeker_delete'),
    path('advisor/', views.advisor_profile, name='advisor'),
]
