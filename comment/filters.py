from rest_framework.filters import BaseFilterBackend


class RootCommentFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('root'):
            return queryset
        else:
            return queryset.filter(root=None)
