from django.urls import path, re_path
from . import views


app_name = 'notification_app'

urlpatterns = [    
    path(
        'api/notification/list',
        views.NotificationListApiView.as_view(),
        ),
    path(
        'api/notification/listPagination',
        views.NotificationListPaginatedApiView.as_view(),
        ),
    path(
        'api/notification/list/search/<kword>/',
        views.NotificationSearchApiView.as_view(),
        ),
    path(
        'api/notification/create/',
        views.NotificationCreateView.as_view(),
        ),
    path(
        'api/usernotification/list',
        views.UserNotificationListApiView.as_view(),
        ),
    path(
        'api/usernotification/listPagination',
        views.UserNotificationListPaginatedApiView.as_view(),
        ),
    path(
        'api/usernotification/list/search/<kword>/',
        views.UserNotificationSearchApiView.as_view(),
        ),
    path(
        'api/usernotification/create/',
        views.UserNotificationCreateView.as_view(),
        )
    ]
