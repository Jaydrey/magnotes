import django_filters
from django_filters import FilterSet

from .models import User


class UserFilter(FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("first_name", "email", "last_name")

