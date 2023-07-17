from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Category Name'))

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    features = models.TextField(verbose_name=_('Features'))
    picture = models.ImageField(upload_to='product_images', verbose_name=_('Image'))
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=_('Price'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))

    def __str__(self):
        return self.name
