from rest_framework import permissions



class Is_Merchant(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'merchant')


class Is_Client(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'client')
    

class Is_OwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.merchant == request.user  

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.merchant == request.user

    