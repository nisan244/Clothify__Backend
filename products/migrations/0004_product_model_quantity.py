# Generated by Django 5.1.3 on 2025-01-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_model_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
