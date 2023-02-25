from django.db import models
from django.urls import reverse


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
        return self.name
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


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('dona', 'Chakana'),
        ('ulgurji', 'Ulgurji'),
    ]
    ORDER_STATUS_CHOICES = [
        ('kutilyapti', 'Kutilyapti'),
        ('tasdiqlandi', 'Tasdiqlandi'),
        ('yetkazildi', 'Yetkazildi'),
        ('bekor qilindi', 'Bekor qilindi'),
    ]
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]
    currency_type = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    order_number = models.CharField(max_length=255, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    types = models.CharField(max_length=255, choices=ORDER_TYPE_CHOICES)
    status = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)





class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def price(self):
        return self.product.selling_price



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


class Transaction(models.Model):
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]
    PAYMENT_CHOICE = [
        ("Naqd", "Naqd"),
        ("Pul o'tkazish", "Pul o'tkazish yo'li bilan")
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=14, choices=PAYMENT_CHOICE)
    currency_type = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class SalesReport(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='sales_reports')
    order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, blank=True, null=True, related_name='sales_reports')
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)
    total_customers = models.IntegerField()
    total_items_sold = models.IntegerField()
    top_selling_products = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


