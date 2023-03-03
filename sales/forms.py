from django import forms
from .models import Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['kompaniya_nomi', 'ismi', 'telefon_raqami', 'manzili']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        # create a helper object
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # define form layout using crispy-forms layout objects
        self.helper.layout = Layout(
            Row(
                Column('ismi', css_class='form-group col-md-6 mb-0'),
                Column('kompaniya_nomi', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('manzili', css_class='form-group col-md-6 mb-0'),
                Column('telefon_raqami', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', "Mijoz qo'shish")
        )
