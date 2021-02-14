from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.notifications.models import UserNotification

from application.notifications.serializers import *

class UserNotificationListApiView(ListAPIView):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer    

    def get_queryset(self):
        return UserNotification.objects.all()

class UserNotificationListPaginatedApiView(ListAPIView):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer
    pagination_class = UserNotificationPaginationSerializer
    def get_queryset(self):
        return UserNotification.objects.all()

class UserNotificationSearchApiView(ListAPIView):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return UserNotification.objects.filter(notification__icontains=kword)
    
class UserNotificationCreateView(CreateAPIView):
    serializer_class = UserNotificationCreateSerializer


