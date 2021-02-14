from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.products.models import LogUpdateProduct

from application.products.serializers import *

# Create your views here.

class LogUpdateListApiView(ListAPIView):
    queryset = LogUpdateProduct.objects.all()
    serializer_class = LogUpdateProductSerializer    

    def get_queryset(self):
        return LogUpdateProduct.objects.all()

class LogUpdateListPaginatedApiView(ListAPIView):
    queryset = LogUpdateProduct.objects.all()
    serializer_class = LogUpdateProductSerializer
    pagination_class = LogUpdateProductPaginationSerializer
    def get_queryset(self):
        return LogUpdateProduct.objects.all()

class LogUpdateSearchApiView(ListAPIView):
    queryset = LogUpdateProduct.objects.all()
    serializer_class = LogUpdateProductSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return LogUpdateProduct.objects.filter(name__icontains=kword)
    
class LogUpdateCreateView(CreateAPIView):
    serializer_class = LogUpdateProductCreateSerializer
