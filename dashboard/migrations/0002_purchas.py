# Generated by Django 4.1.5 on 2023-03-27 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(null=True)),
                ('pur_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendor')),
            ],
        ),
    ]
