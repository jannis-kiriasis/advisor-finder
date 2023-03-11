from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path(
        'signup/',
        views.advisor_signup,
        name='advisor_signup'
    ),
    path(
        'profile/',
        views.advisor_profile,
        name='advisor_profile'
    ),
    path(
        'deactivate/',
        views.deactivate_profile,
        name='deactivate_profile'
    ),
    path(
        'update/',
        views.update_advisor,
        name='update_advisor'
    ),
    path(
        'clients/',
        views.clients_list,
        name='clients'
    ),

    path(
        'clients/<match_id>',
        views.seeker_profile,
        name='client_profile'
    ),
    path(
        'clients/<match_id>/delete/<consultation_id>',
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
