from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import ProductForm
from .models import Product


def homepage(request):
    return render(request=request, template_name="core/index.html")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/add_product.html'
    success_url = reverse_lazy('core:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_update.html'
    success_url = reverse_lazy('core:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'core/product_delete.html'
    success_url = reverse_lazy('core:product_list')


class ProductListView(ListView):
    model = Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'


class ExpenseCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/expense_add.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/expense_update.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseDeleteView(DeleteView):
    model = Product
    template_name = 'core/expense_delete.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseListView(ListView):
    model = Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'
