from django.urls import path
from tasks.views import TaskList, ProjectList, ProjectCreate, ProjectDetail, TaskCreate, TaskDetail

urlpatterns = [

    path('project/', ProjectList.as_view(), name='project'),
    path('project/create/', ProjectCreate.as_view(), name='craete_project'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='detail_project'),
    
    path('tasks/', TaskList.as_view(), name='task'),
    path('tasks/create/', TaskCreate.as_view(), name='craete_task'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='detail_task'),
    
]