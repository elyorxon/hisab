from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import CustomerForm
from .models import Customer


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

