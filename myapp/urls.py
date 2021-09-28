from django.urls import path
from .views import *

urlpatterns = [

    # path("", views.home, name='blog-home'),
    # path("about/", views.about, name='blog-about'),
    path('', regform, name='registration form'),
]
