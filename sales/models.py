from django.db import models


class Customer(models.Model):
    kompaniya_nomi = models.CharField(max_length=255, null=True, blank=True)
    ismi = models.CharField(max_length=255)
    manzili = models.TextField()
    telefon_raqami = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ismi




# Create your models here.
