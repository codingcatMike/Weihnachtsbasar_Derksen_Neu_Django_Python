from django.db import models
from datetime import datetime
from decimal import Decimal

# Create your models here.
class ShoppingItem(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    number = models.PositiveIntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True)

class products(models.Model):
    pronumber = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    shop = models.CharField(max_length=100, default='Unknown')
    price = models.PositiveIntegerField(null=True, blank=True)
    price_happy_hour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.price and not self.price_happy_hour:
            self.price_happy_hour = Decimal(str(self.price)) * Decimal('0.75')
        super().save(*args, **kwargs)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    authentificationCode = models.IntegerField(null=True)

class HappyHour(models.Model):
    is_happy_hour = models.BooleanField(default=False)