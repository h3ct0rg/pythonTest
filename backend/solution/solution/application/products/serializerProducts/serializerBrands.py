from rest_framework import serializers, pagination
from application.products.models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id',
            'name',
            'description')

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')

class BrandPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50
