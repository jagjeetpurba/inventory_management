# Generated by Django 4.1.5 on 2023-03-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_inventory_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchas',
            name='total_amt',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='sales',
            name='total_amount',
            field=models.FloatField(editable=False),
        ),
    ]