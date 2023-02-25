from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView,\
    ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, ExpenseListView, homepage


app_name = "core"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('product/add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('expense/expense_add/', ExpenseCreateView.as_view(), name='expense_add'),
    path('expense/<int:pk>/expense_update/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('product/<int:pk>/expense_delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense_list/', ExpenseListView.as_view(), name='expense_list'),
]
