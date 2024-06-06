from django.shortcuts import render
from rest_framework import generics
from tasks.models import Task, Project
from tasks.serializers import TaskSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner 

class ProjectList(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
    

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated, IsOwner]



class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]
    

