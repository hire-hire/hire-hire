from rest_framework import permissions


class IsDuelModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_duel_moderator
