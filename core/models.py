from django.db import models
from django.urls import reverse

class Kirim(models.Model):
    miqdori = models.PositiveIntegerField()
    sana = models.DateField()

class Chiqim(models.Model):
    miqdori = models.ForeignKey(Kirim, on_delete=models.CASCADE)
    sana = models.DateField()




class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('lt', 'Litr'),
        ('dona', 'Dona'),
        ('m', 'Metr'),
        ('qop', "Qop"),
        ('quti', "Yashik,Qadoq")

    ]
    nomi = models.CharField(max_length=255)
    tavsifi = models.TextField()
    tannarxi = models.DecimalField(max_digits=10, decimal_places=2)
    sotilish_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori = models.PositiveIntegerField()
    ulchov_birligi = models.CharField(choices=UNIT_CHOICES, max_length=20)
    kategoriyasi = models.CharField(max_length=255)
    taminotchi = models.CharField(max_length=255)
    qutidagi_tovar_soni = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomi



class Supplier(models.Model):
    nomi = models.CharField(max_length=255)
    manzili = models.TextField()
    telefon_raqami = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomi


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_restocked_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product


class Expenses(models.Model):
    xarajat_nomi = models.CharField(max_length=255)
    maqsadi = models.TextField()
    miqdori = models.DecimalField(max_digits=10, decimal_places=2)
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]
    valyuta_turi = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Xarajatlar"

    def __str__(self):
        return self.xarajat_nomi

    def get_absolute_url(self):
        return reverse('expense_detail', args=[str(self.id)])





#
# class SalesReport(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='sales_reports')
#     order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='sales_reports')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     total_sales = models.DecimalField(max_digits=10, decimal_places=2)
#     total_profit = models.DecimalField(max_digits=10, decimal_places=2)
#     total_customers = models.IntegerField()
#     total_items_sold = models.IntegerField()
#     top_selling_products = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


