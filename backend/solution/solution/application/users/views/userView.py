from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,    
    )

from application.users.models import User

from application.users.serializers import UserSerializer, UserCreateSerializer, UserPaginationSerializer

# Create your views here.
class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

    def get_queryset(self):
        return User.objects.all()

class UserListPaginatedApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPaginationSerializer
    def get_queryset(self):
        return User.objects.all()

class UserSearchApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        kword = self.kwargs['kword']
        return User.objects.filter(
            name__icontains=kword
            )
    
class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(
            id=pk
            )

class userDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class userUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer