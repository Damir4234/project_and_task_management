from django.shortcuts import render
from rest_framework import generics, status
from users.models import CustomUser 
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения хешированного пароля в бд (если пароль не хешируется -
        пользователь не считается активным и токен авторизации не создается)"""
        
        

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = CustomUser.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)