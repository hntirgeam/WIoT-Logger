from rest_framework import permissions


class IsDeviceOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCSVOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        device_pk = int(view.kwargs.get("pk", None))
        return device_pk in [i.id for i in request.user.devices.all()]
