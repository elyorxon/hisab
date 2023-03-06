from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import CustomerForm, OrderForm
from .models import Customer, Order


def homepage(request):
    return render(request=request, template_name="core/index.html")


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer_add.html'
    success_url = reverse_lazy('sales:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sales/customer_update.html'
    success_url = reverse_lazy('sales:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'sales/customer_delete.html'
    success_url = reverse_lazy('sales:customer_list')


class CustomerListView(ListView):
    model = Customer
    template_name = 'sales/customer_list.html'
    context_object_name = 'customers'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'sales/order_add.html'
    success_url = reverse_lazy('sales:order_list')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'sales/order_update.html'
    success_url = reverse_lazy('sales:order_list')


class OrderDeleteView(DeleteView):
    model = Customer
    template_name = 'sales/order_delete.html'
    success_url = reverse_lazy('sales:order_list')


class OrderListView(ListView):
    model = Customer
    template_name = 'sales/order_list.html'
    context_object_name = 'orders'

