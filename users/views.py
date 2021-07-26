from rest_framework import viewsets,mixins,response

from users import models,serializers


class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


    # def create(self, request, *args, **kwargs):
    #     serializer

