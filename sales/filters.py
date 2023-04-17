import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    tovar_nomi = django_filters.CharFilter(lookup_expr='icontains')
    valyuta_turi = django_filters.CharFilter(lookup_expr='icontains')
    sana = django_filters.DateFilter(field_name='sana', lookup_expr='exact')
    mijoz_ismi = django_filters.CharFilter(lookup_expr='icontains')
    buyurtma_miqdori = django_filters.NumberFilter()
    buyurtma_turi = django_filters.ChoiceFilter(choices=Order.ORDER_TYPE_CHOICES)
    buyurtma_holati = django_filters.ChoiceFilter(choices=Order.ORDER_STATUS_CHOICES)

    class Meta:
        model = Order
        fields = ['tovar_nomi', 'valyuta_turi', 'sana', 'mijoz_ismi', 'buyurtma_miqdori', 'buyurtma_turi', 'buyurtma_holati']
