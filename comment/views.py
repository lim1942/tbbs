from rest_framework import viewsets, mixins,exceptions
from comment import models, serializers,permissions



class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.LoginAcquirePermission,)

    def permission_denied(self, request, message=None, code=None):
        raise exceptions.ValidationError('未登录')
        return super().permission_denied( request, message, code)