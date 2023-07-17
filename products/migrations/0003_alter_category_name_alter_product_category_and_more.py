# Generated by Django 4.2.3 on 2023-07-17 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.TextField(verbose_name='Features'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='product_images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Price'),
        ),
    ]