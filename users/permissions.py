from rest_framework.permissions import BasePermission
from tasks.models import Project


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