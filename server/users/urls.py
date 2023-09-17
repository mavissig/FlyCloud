"""
URL configuration for users project.
"""
from .views import *
from django.urls import path

urlpatterns = [
    path('', session_check),
    path('upload/', upload_file),
    path('<int:user_id>/', personal_account),
    path('<int:user_id>/upload/', upload_file),
]
