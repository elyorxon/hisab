from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',  'description', 'cost_price', 'selling_price', 'quantity', 'unit', 'products_per_box','category','supplier']
        widgets = {
        # 'barcode': forms.TextInput(attrs={'class': 'barcode_field'}),
        'unit': forms.Select(attrs={'class': 'unit_field'}),
    }
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['unit'].choices = Product.UNIT_CHOICES
