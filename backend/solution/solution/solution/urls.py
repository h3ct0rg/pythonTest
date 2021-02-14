"""
Definition of urls for solution.
"""

from datetime import datetime
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='solution')

urlpatterns = [   
    path('admin/', admin.site.urls),
    path('', schema_view),
    re_path('',include('application.users.urls')),
    re_path('',include('application.products.urls')),
    re_path('',include('application.notifications.urls'))
]
