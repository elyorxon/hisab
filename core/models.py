from django.db import models


class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('lt', 'Litr'),
        ('dona', 'Dona'),
        ('m', 'Metr'),
        ('qop', "Qop"),
        ('quti', "Yashik,Qadoq")

    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(choices=UNIT_CHOICES, max_length=20)
    category = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    products_per_box = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=255)
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
        ('shipped', 'Shipped'),
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
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Expenses(models.Model):
    expanse_name = models.CharField(max_length=255)
    purpose = models.TextField()
    payment_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]
    currency_type = models.CharField(max_length=3, choices=CURRENCY_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expanse_name


class Transaction(models.Model):
    CURRENCY_TYPE_CHOICES = [
        ('USD', 'US Dollar'),
        ('UZS', 'Uzbekistan Sum'),
        ('RUB', 'Russian Ruble'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=255)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='transactions')
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


