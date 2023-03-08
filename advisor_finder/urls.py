"""advisor_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('advisors/', include('advisors.urls')),
    path('seekers/', include('seekers.urls')),
    path('match/', include('matches.urls')),
    path('', include('home.urls')),
    path('checkout/', include('checkout.urls')),
    path('sitemap.xml', views.sitemap,),
    path('robots.txt', views.robots),
]

handler404 = 'advisor_finder.views.handler404'
handler500 = 'advisor_finder.views.handler500'
