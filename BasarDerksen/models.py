from django.db import models
from datetime import datetime
# Create your models here.
class ShoppingItem(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    number = models.PositiveIntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True)  # add this field



