from rest_framework import serializers, pagination
from application.products.models import LogUpdateProduct

class LogUpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUpdateProduct
        fields = ('product',
            'user')

class LogUpdateProductPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50

class LogUpdateProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUpdateProduct
        fields = ('__all__')
