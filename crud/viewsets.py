from rest_framework import viewsets

from crud import models, serializers, filters


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = filters.UserFilterSet
