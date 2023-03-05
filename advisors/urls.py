from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.advisor_signup, name='advisor_signup'),
    path('profile/', views.advisor_profile, name='advisor_profile'),
    path('deactivate/', views.deactivate_profile, name='deactivate_profile'),
    path('clients/', views.clients_list, name='clients'),
    # path(
    #     'matches/client/<match_id>',
    #     views.seeker_profile,
    #     name='match_profile'
    # ),
    # path(
    #     'matches/client/<match_id>/delete/<consultation_id>',
    #     views.match_delete_consultation,
    #     name='match_delete_consultation'
    # ),

    path(
        'clients/client/<match_id>',
        views.seeker_profile,
        name='client_profile'
    ),
    path(
        'clients/client/<match_id>/delete/<consultation_id>',
        views.client_delete_consultation,
        name='client_delete_consultation'
    ),

    path(
        'appointments/',
        views.consultation_list,
        name='consultations'
    ),
    path(
        'appointments/delete/<consultation_id>',
        views.delete_consultation,
        name='delete'
    ),

]
