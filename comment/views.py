from rest_framework import viewsets,response
from comment import models, serializers,permissions,filters,pagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.CreateLoginAcquirePermission,)
    filter_backends = (filters.RootCommentFilter,)
    pagination_class = pagination.CommentPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        item = dict(serializer.data)
        child_queryset = models.Comment.objects.filter(root=item['id'])
        item['child_con'] = self.get_serializer(child_queryset, many=True).data
        return response.Response(item)
