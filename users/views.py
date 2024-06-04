from django.shortcuts import render
from rest_framework import generics
from users.models import CustomUser 
from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
