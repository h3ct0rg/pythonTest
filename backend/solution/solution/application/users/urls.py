from django.urls import path, re_path
from .views import userView

app_name = 'user_app'

urlpatterns = [
    path(
        'api/user/list',
        userView.UserListApiView.as_view(),
        ),
    path(
        'api/user/listPage',
        userView.UserListPaginatedApiView.as_view(),
        ),
    path(
        'api/user/list/search/<kword>/',
        userView.UserSearchApiView.as_view(),
        ),
    path(
        'api/user/create/',
        userView.UserCreateView.as_view(),
        ),
    path(
        'api/user/update/<pk>',
        userView.userUpdateView.as_view(),
        ),
    path(
        'api/user/detail/<pk>',
        userView.UserDetailView.as_view(),
        ),
    path(
        'api/user/delete/<pk>',
        userView.userDeleteView.as_view(),
        )
    ]