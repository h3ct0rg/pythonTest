"""
Definition of urls for solution.
"""

from datetime import datetime
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [   
    path('admin/', admin.site.urls),
    re_path('',include('application.users.urls')),
    re_path('',include('application.products.urls')),
]
