from django.contrib import admin
from market.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'balance', 'price']
    list_filter = ['name', 'category', 'balance', 'price']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'balance', 'price']


admin.site.register(Product, ProductAdmin)
