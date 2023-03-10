from django import forms
from .models import Customer, Order, Transaction
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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['tovar', 'valyuta_turi', 'mijoz', 'sana', 'buyurtma_miqdori', 'buyurtma_turi', 'buyurtma_holati']
        widgets = {
            'sana': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'buyurtma_holati': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_buyurtma_miqdori(self):
        buyurtma_miqdori = self.cleaned_data['buyurtma_miqdori']
        if buyurtma_miqdori <= 0:
            raise forms.ValidationError("Buyurtma miqdori noldan katta bo'lishi kerak.")
        return buyurtma_miqdori

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Row(
                Column('tovar', css_class='form-group col-md-4 mb-0'),
                Column('valyuta_turi', css_class='form-group col-md-4 mb-0'),
                Column('sana', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mijoz', css_class='form-group col-md-6 mb-0'),
                Column('buyurtma_miqdori', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('buyurtma_turi', css_class='form-group col-md-6 mb-0'),
                Column('buyurtma_holati', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', "Buyurtma qo'shish")
        )

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['buyurtma', 'mijoz', 'summa', 'sana', 'holati', 'tulov_turi', 'valyuta_turi']

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        # create a helper object
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # define form layout using crispy-forms layout objects
        self.helper.layout = Layout(
            Row(
                Column('buyurtma', css_class='form-group col-md-6 mb-0'),
                Column('mijoz', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('summa', css_class='form-group col-md-6 mb-0'),
                Column('sana', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('holati', css_class='form-group col-md-4 mb-0'),
                Column('tulov_turi', css_class='form-group col-md-4 mb-0'),
                Column('valyuta_turi', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', "To'lov qo'shish")
        )
