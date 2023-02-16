from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.advisor_signup, name='advisor_signup'),
    path('profile/', views.advisor_profile, name='advisor_profile'),
    path('deactivate/', views.deactivate_profile, name='deactivate_profile'),

]
