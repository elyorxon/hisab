from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView, homepage


app_name = "sales"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('customer/customer_add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customer/<int:pk>/customer_update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/customer_delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),

]
