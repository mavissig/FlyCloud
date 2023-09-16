"""
URL configuration for users project.
"""
from .views import *
from django.urls import path

urlpatterns = [
    path('', session_check),
    path('upload/', upload_file),
    # path(':<int:int_param>/', debug_resp),
]
