# Generated by Django 4.1.5 on 2023-03-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_customer_remove_sales_customer_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
