from rest_framework import serializers, pagination
from application.notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id',
            'notification',
            'dateGenerated')

class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('__all__')

class NotificationPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50
