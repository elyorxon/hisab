from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'description', 'cost_price', 'selling_price', 'quantity', 'unit', 'products_per_box','category','supplier','min_stock','max_stock','barcode']
        widgets = {
        'barcode': forms.TextInput(attrs={'class': 'barcode_field'}),
        'unit': forms.Select(attrs={'class': 'unit_field'}),
    }
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['unit'].choices = Product.UNIT_CHOICES
