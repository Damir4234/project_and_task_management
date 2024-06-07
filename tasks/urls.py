from django.urls import path
from tasks.views import TaskListAPIView, ProjectListAPIView, ProjectCreateAPIView, TaskCreateAPIView, ProjectRetrieveAPIView, ProjectUpdateAPIView, ProjectDeleteAPIView, TaskRetrieveAPIView, TaskUpdateAPIView, TaskDeleteAPIView

urlpatterns = [

    path('project/', ProjectListAPIView.as_view(), name='projects'),
    path('project/create/', ProjectCreateAPIView.as_view(), name='create_project'),
    path('project/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='detail_project'),
    path('project/<int:pk>/update/', ProjectUpdateAPIView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', ProjectDeleteAPIView.as_view(), name='delete_project'),

    path('tasks/', TaskListAPIView.as_view(), name='tasks'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='create_task'),
    path('tasks/<int:pk>/', TaskRetrieveAPIView.as_view(), name='detail_task'),
    path('tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='delete_task'),
    
    
]