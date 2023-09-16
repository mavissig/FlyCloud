"""
URL configuration for flycloud project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("auths.urls")),
    path('user/', include("users.urls")),
]
