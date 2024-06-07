from django.shortcuts import render
from rest_framework import generics
from tasks.models import Task, Project
from tasks.serializers import TaskSerializer, ProjectSerializer
from users.permissions import IsOwner, IsProjectOwner, IsAssignee, IsProjectOwnerDelete


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectListAPIView(generics.ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

class ProjectRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    


class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]


class ProjectDeleteAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]

    
    


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsProjectOwner]

    


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    


class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAssignee]


class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsProjectOwnerDelete]
    





    

