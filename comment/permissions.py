from rest_framework.permissions import BasePermission


class LoginAcquirePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        # 登录后才能发布
        if request.method == "POST":
            if request.user_info:
                return True


