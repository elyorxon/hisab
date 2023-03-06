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
    valyuta_turi = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    buyurtma_raqami = models.CharField(max_length=255, primary_key=True)
    mijoz = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sana = models.DateField()
    buyurtma_miqdori = models.PositiveIntegerField(max_length=16)
    buyurtma_turi = models.CharField(max_length=255, choices=ORDER_TYPE_CHOICES)
    buyurtma_holati = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)





class OrderItem(models.Model):
    buyurtma = models.ForeignKey(Order, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Product, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()

    def price(self):
        return self.product.sotilish_narxi
