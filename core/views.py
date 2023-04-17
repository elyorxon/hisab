from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ProductForm, ExpensesForm, KirimForm, ChiqimForm
from .models import Product, Expenses, Kirim, Chiqim


def homepage(request):
    return render(request=request, template_name="core/index.html")


class KirimCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/add_kirim.html'
    success_url = reverse_lazy('core:kirim_list')


class KirimUpdateView(UpdateView):
    model = Kirim
    form_class = KirimForm
    template_name = 'core/kirim_update.html'
    success_url = reverse_lazy('core:kirim_list')


class KirimDeleteView(DeleteView):
    model = Kirim
    template_name = 'core/kirim_delete.html'
    success_url = reverse_lazy('core:kirim_list')


class KirimListView(ListView):
    model = Kirim
    template_name = 'core/kirim_list.html'
    context_object_name = 'kirims'
    paginate_by = 10  # number of products per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kirims = context['kirims']
        paginator = Paginator(kirims, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            kirims = paginator.page(page)
        except PageNotAnInteger:
            kirims = paginator.page(1)
        except EmptyPage:
            kirims = paginator.page(paginator.num_pages)

        context['kirims'] = kirims
        return context

class ChiqimCreateView(CreateView):
    model = Chiqim
    form_class = ChiqimForm
    template_name = 'core/add_chiqim.html'
    success_url = reverse_lazy('core:chiqim_list')


class ChiqimUpdateView(UpdateView):
    model = Chiqim
    form_class = ChiqimForm
    template_name = 'core/chiqim_update.html'
    success_url = reverse_lazy('core:chiqim_list')


class ChiqimDeleteView(DeleteView):
    model = Chiqim
    template_name = 'core/chiqim_delete.html'
    success_url = reverse_lazy('core:chiqim_list')


class ChiqimListView(ListView):
    model = Chiqim
    template_name = 'core/chiqim_list.html'
    context_object_name = 'chiqims'
    paginate_by = 10  # number of products per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chiqims = context['chiqims']
        paginator = Paginator(chiqims, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            chiqims = paginator.page(page)
        except PageNotAnInteger:
            chiqims = paginator.page(1)
        except EmptyPage:
            chiqims = paginator.page(paginator.num_pages)

        context['chiqims'] = chiqims
        return context


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
