
from django.contrib import admin
# Register your models here.
from app1.models import Category,Customer,Order,Products


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.

admin.site.register(Category),
admin.site.register(Products,AdminProduct)
admin.site.register(Customer)
admin.site.register(Order)