from django.contrib.auth.models import User
from django_filters import rest_framework as filters


# Filter that demonstrates how django-filters FilterSets work.
class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='iendswith')
    first_name = filters.CharFilter(lookup_expr='istartswith')
    # Below: when extracting parts of a date, use a NumberFilter not a Date/DateTimeFilter
    year_joined = filters.NumberFilter(field_name='date_joined', lookup_expr='year')
    month_joined = filters.NumberFilter(field_name='date_joined', lookup_expr='month')
    day_joined = filters.NumberFilter(field_name='date_joined', lookup_expr='day')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']