"""
URL configuration for kaizntree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from kaizn.views import login_page,register_page,add_item,display_items
from rest_framework import routers


urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/',register_page,name='register'),
    path('add_item/',add_item,name='add_item'),
    path('dashboard/',display_items,name='display_items'),
]
