from django.contrib import admin
from django.urls import path
from libsys import views as libsys_views

app_name='ebooksys'

urlpatterns = [
    path('', libsys_views.index),
    path('search/', libsys_views.search),
]
