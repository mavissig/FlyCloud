"""
URL configuration for auth.
"""
from .models import *
from django.urls import path

urlpatterns = [
    path('', auths_user),
    path('reg/', registry_user)
]