# Created this file (rul.py) for URL mapping or URL configuration
# want to import path from django

from os import name
from django.urls import path    # imported path from django.urls
from . import views              # imported views

urlpatterns = [
    path('', views.index, name='index '),           # go to the views.py and create metod 'index'
                                                   # index is a function from views.py
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register')
]
