from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.products.models import Brand

from application.products.serializers import *

class BrandListApiView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer    

    def get_queryset(self):
        return Brand.objects.all()

class BrandListPaginatedApiView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = BrandPaginationSerializer
    def get_queryset(self):
        return Brand.objects.all()

class BrandSearchApiView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return Brand.objects.filter(name__icontains=kword)
    
class BrandCreateView(CreateAPIView):
    serializer_class = BrandCreateSerializer
