from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .forms import ProductForm, ExpensesForm
from .models import Product, Expenses


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
    paginate_by = 10  # number of products per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['products']
        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context

class ExpenseCreateView(CreateView):
    model = Expenses
    form_class = ExpensesForm
    template_name = 'core/expense_add.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseUpdateView(UpdateView):
    model = Expenses
    form_class = ExpensesForm
    template_name = 'core/expense_update.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseDeleteView(DeleteView):
    model = Expenses
    form_class = ExpensesForm
    template_name = 'core/expense_delete.html'
    success_url = reverse_lazy('core:expense_list')


class ExpenseListView(ListView):
    model = Expenses
    template_name = 'core/expense_list.html'
    context_object_name = 'expenses'

    paginate_by = 10  # number of products per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = context['expenses']
        paginator = Paginator(expenses, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)

        context['expenses'] = expenses
        return context