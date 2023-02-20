from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView
from . import views

app_name = "core"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/', ProductListView.as_view(), name='product_list'),
    # ...
]
