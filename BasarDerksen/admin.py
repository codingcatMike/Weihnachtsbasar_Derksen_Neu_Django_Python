from django.contrib import admin
from .models import ShoppingItem
from .models import *
# Register your models here.
admin.site.register(ShoppingItem)
admin.site.register(products)
admin.site.register(User)
admin.site.register(HappyHour)