from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost_price', 'selling_price', 'quantity', 'unit', 'products_per_box',
                  'category', 'supplier']
        widgets = {
            'unit': forms.Select(attrs={'class': 'unit_field'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['unit'].choices = Product.UNIT_CHOICES

        # create a helper object
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # define form layout using crispy-forms layout objects
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cost_price', css_class='form-group col-md-6 mb-0'),
                Column('selling_price', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('quantity', css_class='form-group col-md-6 mb-0'),
                Column('unit', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('products_per_box', css_class='form-group col-md-6 mb-0'),
                Column('supplier', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
