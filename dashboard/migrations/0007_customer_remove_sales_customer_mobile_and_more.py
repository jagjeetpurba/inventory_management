# Generated by Django 4.1.5 on 2023-03-28 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_purchas_total_amt_alter_sales_total_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('customer_mobile', models.PositiveIntegerField(null=True)),
                ('customer_add', models.CharField(max_length=150, null=True)),
                ('customer_pincode', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='sales',
            name='customer_mobile',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.customer'),
        ),
    ]
