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
    tovar = models.ForeignKey(Product, on_delete=models.CASCADE)
    valyuta_turi = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    mijoz = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sana = models.DateField()
    buyurtma_miqdori = models.PositiveIntegerField(default=0)
    buyurtma_turi = models.CharField(max_length=255, choices=ORDER_TYPE_CHOICES)
    buyurtma_holati = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)


    def __str__(self):
        return self.tovar


class Transaction(models.Model):
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]
    PAYMENT_CHOICE = [
        ("Naqd", "Naqd"),
        ("Pul o'tkazish", "Pul o'tkazish yo'li bilan"),

    ]
    PAYMENT_STATUS = [
        ("To'liq to'landi", "To'liq to'landi"),
        ("Qisman to'landi", "Qisman to'lanmadi"),
        ("To'lanmadi", "Umuman to'lanmadi"),
    ]
    buyurtma = models.ForeignKey(Order, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    summa = models.PositiveIntegerField()
    sana = models.DateField()
    holati = models.CharField(max_length=20, choices=PAYMENT_STATUS)
    tulov_turi = models.CharField(max_length=14, choices=PAYMENT_CHOICE)
    valyuta_turi = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
