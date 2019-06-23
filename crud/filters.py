from django_filters import filterset

from crud import choices, models


class UserFilterSet(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=choices.LIKE)

    class Meta:
        model = models.User
        fields = ['name']
