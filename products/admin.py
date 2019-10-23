from django.contrib import admin
from .models import Product
from .models import Offer

# This will create a table under Product section
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

# This will create a table under Offer section
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

# Register your models here.
# Registered models can be managed via GUI on browser
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)