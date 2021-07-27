from rest_framework import viewsets, response
from django_filters.rest_framework import DjangoFilterBackend

from comment import models, serializers, permissions, filters, pagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.CreateLoginAcquirePermission,)
    pagination_class = pagination.CommentPagination
    filter_backends = (filters.RootCommentFilter, DjangoFilterBackend)
    filterset_fields = {'root': ['exact'],
                        'parent': ['exact'],
                        'user': ['exact'],
                        'created_time': ['gte', 'lte'],
                        }
