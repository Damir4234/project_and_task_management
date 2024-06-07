from rest_framework.permissions import BasePermission
from tasks.models import Project, Task


class IsOwner(BasePermission):
    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
    

class IsProjectOwner(BasePermission):

    message = "Вы не являетесь владельцем проекта"
    def has_permission(self, request, view):
        if request.method == 'POST':
            project_id = request.data.get('project')
            if not project_id:
                return False
            try:
                project = Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                return False
            return project.owner == request.user
        return True
    

class IsProjectOwnerDelete(BasePermission):
    message = "Вы не являетесь владельцем проекта"

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            task_id = view.kwargs.get('pk')
            try:
                task = Task.objects.get(pk=task_id)
                project = task.project
            except Task.DoesNotExist:
                return False
            return project.owner == request.user
        return True
    

class IsAssignee(BasePermission):
    message = "Доступно исполнителю"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.assignee
    

# class IsAssigneeAndCanChangeStatus(BasePermission):
#     message = "Только исполнитель может изменять статус задачи"

#     def has_permission(self, request, view):
#         if request.method in ['PATCH', 'PUT']:
#             task_id = view.kwargs.get('pk')
#             try:
#                 task = Task.objects.get(pk=task_id)
#             except Task.DoesNotExist:
#                 return False

#             if task.assignee != request.user:
#                 return False

#             if 'status' in request.data and len(request.data) == 1:
#                 return True
#             return False
#         return True