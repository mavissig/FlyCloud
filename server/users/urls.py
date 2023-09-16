"""
URL configuration for users project.
"""
from .models import *
from django.urls import path

urlpatterns = [
    path('', session_check)
]
