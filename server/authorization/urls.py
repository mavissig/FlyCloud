"""
URL configuration for auth.
"""
from .models import *
from django.urls import path

app_name = 'authorization'

urlpatterns = [
    path('', authorization_user, name='authorization_user'),
]
