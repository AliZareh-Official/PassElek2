from django.db import models

# Create your models here.
from django.contrib import admin
from .models import Product,Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
