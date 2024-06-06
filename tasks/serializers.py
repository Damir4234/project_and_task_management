from rest_framework import serializers
from tasks.models import Task, Project




class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['name', 'description', 'date_of_creation', 'last_modified', 'owner']
        read_only_fields = ['date_of_creation', 'last_modified', 'owner']


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'


