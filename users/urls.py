from django.urls import path
from users.views import UserCreate

urlpatterns = [

    
    path('user/create/', UserCreate.as_view(), name='create_user'),
    
    
]