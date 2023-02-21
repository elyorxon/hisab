from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, homepage


app_name = "core"

urlpatterns = [
    path("", homepage, name="homepage"),
    path('product/add_product/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/', ProductListView.as_view(), name='product_list'),
    # ...
]
