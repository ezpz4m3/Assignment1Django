from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Product, Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ["name","price"]


admin.site.register(User)
admin.site.register(Product, ProductAdmin)