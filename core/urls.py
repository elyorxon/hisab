from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView,\
    ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, ExpenseListView, homepage, KirimCreateView, \
    KirimUpdateView, KirimDeleteView, KirimListView, ChiqimCreateView, ChiqimUpdateView, ChiqimDeleteView, \
    ChiqimListView


app_name = "core"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('product/add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('kirim/add_kirim/', KirimCreateView.as_view(), name='add_kirim'),
    path('kirim/<int:pk>/kirim_update/', KirimUpdateView.as_view(), name='kirim_update'),
    path('kirim/<int:pk>/kirim_delete/', KirimDeleteView.as_view(), name='kirim_delete'),
    path('kirim_list/', KirimListView.as_view(), name='kirim_list'),
    path('chiqim/add_chiqim/', ChiqimCreateView.as_view(), name='add_chiqim'),
    path('chiqim/<int:pk>/chiqim_update/', ChiqimUpdateView.as_view(), name='chiqim_update'),
    path('chiqim/<int:pk>/chiqim_delete/', ChiqimDeleteView.as_view(), name='chiqim_delete'),
    path('chiqim_list/', ChiqimListView.as_view(), name='chiqim_list'),
    path('expense/expense_add/', ExpenseCreateView.as_view(), name='expense_add'),
    path('expense/<int:pk>/expense_update/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('product/<int:pk>/expense_delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('expense_list/', ExpenseListView.as_view(), name='expense_list'),
]
