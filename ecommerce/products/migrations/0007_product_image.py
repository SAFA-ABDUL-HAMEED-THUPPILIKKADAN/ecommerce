# Generated by Django 4.2.6 on 2023-12-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_productss_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
