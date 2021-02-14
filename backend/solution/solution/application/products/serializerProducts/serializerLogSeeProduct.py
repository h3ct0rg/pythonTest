from rest_framework import serializers, pagination
from application.products.models import LogSeeProduct

class LogSeeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSeeProduct
        fields = ('product',
            'dateView')

class LogSeeProductPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50

class LogSeeProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogSeeProduct
        fields = ('__all__')
