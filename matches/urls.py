from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.match, name='match'),
    path(
        'select-advisor/<advisor_id>', views.create_match, name='create_match')
]
