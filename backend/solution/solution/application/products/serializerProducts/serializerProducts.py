from rest_framework import serializers, pagination
from application.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
            'sku',
            'name',
            'price',
            'brand')

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class ProductPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50

