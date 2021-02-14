from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, CreateAPIView

from application.products.models import LogSeeProduct

from application.products.serializers import *

# Create your views here.

class LogSeeListApiView(ListAPIView):
    queryset = LogSeeProduct.objects.all()
    serializer_class = LogSeeProductSerializer    

    def get_queryset(self):
        return LogSeeProduct.objects.all()

class LogSeeListPaginatedApiView(ListAPIView):
    queryset = LogSeeProduct.objects.all()
    serializer_class = LogSeeProductSerializer
    pagination_class = LogSeeProductPaginationSerializer
    def get_queryset(self):
        return LogSeeProduct.objects.all()

class LogSeeSearchApiView(ListAPIView):
    queryset = LogSeeProduct.objects.all()
    serializer_class = LogSeeProductSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return LogSeeProduct.objects.filter(name__icontains=kword)
    
class LogSeeCreateView(CreateAPIView):
    serializer_class = LogSeeProductCreateSerializer

