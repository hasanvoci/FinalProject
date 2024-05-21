from rest_framework.permissions import BasePermission


class IsHR(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role == 'hr'

    def has_object_permission(self, request, view, obj):
        return True


class IsEmployee(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

