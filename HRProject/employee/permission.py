from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsHRorIsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.role.role == 'hr'
