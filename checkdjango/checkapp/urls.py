"""mydjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import checkapp.views as checkapp


from django.contrib import admin
from django.urls import path, include

app_name = 'checkapp'

urlpatterns = [
    path('', checkapp.index),
    path('catalog/', checkapp.catalog),
    path('catalog/category/<int:pk>/', checkapp.group, name='group'),
    path('catalog/category/album/<int:pk>/', checkapp.album, name='album'),
    path('catalog/category/album/song/<int:pk>/', checkapp.song, name='song'),
    path('catalog/category/album/song/song_page/<int:pk>/', checkapp.song_page, name='song_page'),




]