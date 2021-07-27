from rest_framework.filters import BaseFilterBackend


class RootCommentFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(root=None)
