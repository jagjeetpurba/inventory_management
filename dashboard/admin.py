from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)
admin.site.site_header= 'JagVentory Dashboard'

class PurchasAdmin(admin.ModelAdmin):
    search_fields=['product__name', 'product__id']
    list_display=['id', 'product', 'qty', 'price', 'total_amt', 'vendor', 'pur_date']

class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__name', 'product__id']
    list_display=['id','product', 'pur_qty', 'sale_qty', 'total_bal_qty', 'sales_date', 'pur_date']

class SaleAdmin(admin.ModelAdmin):
    search_fields=['product__name', 'product__id']
    list_display=['id', 'customer_name', 'product', 'qty', 'price', 'total_amount', 'sales_date']

class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

#class CustomerAdmin(admin.ModelAdmin):
 #   search_fields=['customer_name', 'customer_mobile', 'customer_pincode']
  #  list_display=['id', 'customer_name', 'customer_mobile', 'customer_add', 'customer_pincode']

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Sales, SaleAdmin)
admin.site.register(Purchas, PurchasAdmin)
admin.site.register(Vendor)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Customer, CustomerAdmin)


