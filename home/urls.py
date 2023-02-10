from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('advisor-or-seeker/', views.advisor_seeker, name='choice')

]
