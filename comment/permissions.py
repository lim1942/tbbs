from rest_framework.permissions import BasePermission


class CreateLoginAcquirePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        # 不可以修改删除
        return False

    def has_permission(self, request, view):
        # 只有已经登陆用户可以创建
        if request.method == "POST":
            if request.user_info:
                return True
        else:
            return True


