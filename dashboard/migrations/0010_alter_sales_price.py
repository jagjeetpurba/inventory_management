# Generated by Django 4.1.5 on 2023-03-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_remove_sales_customer_sales_cust_add_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.FloatField(editable=False),
        ),
    ]