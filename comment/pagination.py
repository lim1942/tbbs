from rest_framework.pagination import PageNumberPagination


class CommentPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 20
    page_size = 10