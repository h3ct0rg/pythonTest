from rest_framework import serializers, pagination
from application.notifications.models import UserNotification

class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ('id',
            'notification',
            'dateGenerated')

class UserNotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ('__all__')

class UserNotificationPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50
