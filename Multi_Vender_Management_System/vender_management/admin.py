from django.contrib import admin
from .models import vendor,purchase_order
# Register your models here.
admin.site.register(vendor)
admin.site.register(purchase_order)