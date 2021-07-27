from rest_framework import viewsets
from comment import models, serializers,permissions


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.LoginAcquirePermission,)

