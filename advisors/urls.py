from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.advisor_signup, name='advisor_signup'),
    path('profile/', views.advisor_profile, name='advisor_profile'),
    path('deactivate/', views.deactivate_profile, name='deactivate_profile'),
    path('matches/', views.matches_list, name='matches'),
    path('clients/', views.clients_list, name='clients'),
    path('matches/clients/<match_id>', views.seeker_profile, name='seeker_profile'),

]
