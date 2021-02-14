from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.products.models import Product

from application.products.serializers import *

class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

    def get_queryset(self):
        return Product.objects.all()

class ProductListPaginatedApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginationSerializer
    def get_queryset(self):
        return Product.objects.all()

class ProductSearchApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Product.objects.filter(name__icontains=kword)
    
class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer
