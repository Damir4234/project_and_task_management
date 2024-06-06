from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Доступно владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner