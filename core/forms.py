from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nomi', 'tavsifi', 'tannarxi', 'sotilish_narxi', 'miqdori', 'ulchov_birligi', 'qutidagi_tovar_soni',
                  'kategoriyasi', 'taminotchi']
        widgets = {
            'ulchov_birligi': forms.Select(attrs={'class': 'unit_field'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['ulchov_birligi'].choices = Product.UNIT_CHOICES

        # create a helper object
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # define form layout using crispy-forms layout objects
        self.helper.layout = Layout(
            Row(
                Column('nomi', css_class='form-group col-md-6 mb-0'),
                Column('kategoriyasi', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tavsifi', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tannarxi', css_class='form-group col-md-6 mb-0'),
                Column('sotilish_narxi', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('miqdori', css_class='form-group col-md-6 mb-0'),
                Column('ulchov_birligi', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('qutidagi_tovar_soni', css_class='form-group col-md-6 mb-0'),
                Column('taminotchi', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', "Tovar qo'shish")
        )
