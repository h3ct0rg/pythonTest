from django.urls import path, re_path
from . import views


app_name = 'product_app'

urlpatterns = [
    path(
        'api/product/list',
        views.ProductListApiView.as_view(),
        ),
    path(
        'api/product/listPagination',
        views.ProductListPaginatedApiView.as_view(),
        ),
    path(
        'api/product/list/search/<kword>/',
        views.ProductSearchApiView.as_view(),
        ),
    path(
        'api/product/create/',
        views.ProductCreateView.as_view(),
        ),
    path(
        'api/brand/list',
        views.BrandListApiView.as_view(),
        ),
    path(
        'api/brand/listPagination',
        views.BrandListPaginatedApiView.as_view(),
        ),
    path(
        'api/brand/list/search/<kword>/',
        views.BrandSearchApiView.as_view(),
        ),
    path(
        'api/brand/create/',
        views.BrandCreateView.as_view(),
        ),
    path(
        'api/logupdateproduct/list',
        views.LogUpdateListApiView.as_view(),
        ),
    path(
        'api/logupdateproduct/listPagination',
        views.LogUpdateListPaginatedApiView.as_view(),
        ),
    path(
        'api/logupdateproduct/list/search/<kword>/',
        views.LogUpdateSearchApiView.as_view(),
        ),
    path(
        'api/logupdateproduct/create/',
        views.LogUpdateCreateView.as_view(),
        ),
    path(
        'api/logseeproduct/list',
        views.LogSeeListApiView.as_view(),
        ),
    path(
        'api/logseeproduct/listPagination',
        views.LogSeeListPaginatedApiView.as_view(),
        ),
    path(
        'api/logseeproduct/list/search/<kword>/',
        views.LogSeeSearchApiView.as_view(),
        ),
    path(
        'api/logseeproduct/create/',
        views.LogSeeCreateView.as_view(),
        )
    ]
