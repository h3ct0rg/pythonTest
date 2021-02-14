from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.notifications.models import Notification

from application.notifications.serializers import *

class NotificationListApiView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer    

    def get_queryset(self):
        return Notification.objects.all()

class NotificationListPaginatedApiView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = NotificationPaginationSerializer
    def get_queryset(self):
        return Notification.objects.all()

class NotificationSearchApiView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Notification.objects.filter(notification__icontains=kword)
    
class NotificationCreateView(CreateAPIView):
    serializer_class = NotificationCreateSerializer

