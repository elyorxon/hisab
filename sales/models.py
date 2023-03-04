from django.db import models
from core.models import Product

class Customer(models.Model):
    kompaniya_nomi = models.CharField(max_length=255, null=True, blank=True)
    ismi = models.CharField(max_length=255)
    manzili = models.TextField()
    telefon_raqami = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ismi


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
