from django_filters import filterset

from crud import models


class UserFilterSet(filterset.FilterSet):
    class Meta:
        model = models.User
        fields = '__all__'
