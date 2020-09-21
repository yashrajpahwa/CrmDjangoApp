import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class orderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created",
                            lookup_expr='gte', label='Start Date')
    # start_date.widget = DateFilter(
    #     attrs={id: 'datepicker'})
    end_date = DateFilter(field_name="date_created",
                          lookup_expr='lte', label='End Date')
    note = CharFilter(field_name="note",
                      lookup_expr='icontains', label='Order Notes')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']

        # widgets = {'start_date': DateFilter(attrs={'id': 'datepicker'})}
