from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView, homepage, \
    OrderCreateView, OrderUpdateView, OrderListView, OrderDeleteView

app_name = "sales"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('customer/customer_add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customer/<int:pk>/customer_update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/customer_delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('order/order_add/', OrderCreateView.as_view(), name='order_add'),
    path('order/<int:pk>/order_update/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/order_delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('order_list/', OrderListView.as_view(), name='order_list'),

]
