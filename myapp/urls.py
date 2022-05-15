from django.urls import path
from django.conf.urls import url
from . import views
from .views import *
from django.contrib import admin

urlpatterns = [

    path('', urlchecker, name='base page')

]
