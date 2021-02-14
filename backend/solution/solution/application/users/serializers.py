from rest_framework import serializers, pagination
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            'id',
            'name',
            'userName',
            'role'
            )

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserPaginationSerializer(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 50