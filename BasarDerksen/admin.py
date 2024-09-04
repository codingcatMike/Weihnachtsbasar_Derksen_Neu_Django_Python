from django.contrib import admin
from .models import ShoppingItem
from .models import products
# Register your models here.
admin.site.register(ShoppingItem)
admin.site.register(products)