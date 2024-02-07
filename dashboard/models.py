from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum



# Create your models here.

class Vendor(models.Model):
    name= models.CharField(max_length=50)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=20)
    pin_code= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name= models.CharField(max_length=20, null=True)
    quantity= models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Product'

    def get_available_quantity(product):
        total_sales = Sales.objects.filter(product=product).aggregate(total_sales=Sum('qty'))['total_sales'] or 0
        total_purchase = Purchas.objects.filter(product=product).aggregate(total_purchase=Sum('qty'))['total_purchase'] or 0
        available_quantity = total_purchase - total_sales
        return available_quantity
    

class Purchas(models.Model):
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty= models.IntegerField(null=True)
    pur_date= models.DateTimeField(auto_now_add=True)
    price=models.FloatField()
    total_amt= models.FloatField(editable=False)

    class Meta:
        verbose_name_plural='Purchase'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.total_amt=self.qty*self.price
        super(Purchas, self).save(*args, **kwargs)

        inventory= Inventory.objects.filter(product= self.product).order_by('-id').first()
        if inventory:
            totalBal= inventory.total_bal_qty+self.qty
        else:
            totalBal= self.qty
        
        Inventory.objects.create(
            product= self.product,
            purchas= self,    
            sales= None,
            pur_qty= self.qty,
            sale_qty= None,
            total_bal_qty= totalBal
        )

class Customer(models.Model):
    customer_name= models.CharField(max_length=100, null=True)
    customer_mobile=models.PositiveIntegerField(null=True)
    customer_add= models.CharField(max_length=150, null=True)
    customer_pincode= models.IntegerField()

    def __str__(self):
        return self.customer_name
    
class Sales(models.Model):
    customer_name= models.CharField(max_length=50, null=True)
    customer_mob= models.IntegerField(null=True)
    cust_add= models.CharField(max_length=150, null=True, default='Indore')
    product= models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty= models.IntegerField(null=True)
    price= models.FloatField()
    staff= models.ForeignKey(User, models.CASCADE, null=True)
    total_amount= models.FloatField(editable=False)
    sales_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Sale'

    def __str__(self):
        return self.product.name
    
    def clean(self):
        inventory= Inventory.objects.filter(product= self.product).order_by('-id').first()
        if inventory:
            if self.qty > inventory.total_bal_qty:
                raise ValidationError("Sale quantity cannot be greater than available quantity")

    def save(self, *args, **kwargs):
        self.total_amount=self.qty*self.price
        super(Sales, self).save(*args, **kwargs)

        inventory= Inventory.objects.filter(product= self.product).order_by('-id').first()
        if inventory:
            totalBal= inventory.total_bal_qty-self.qty
        
        Inventory.objects.create(
            product= self.product,
            purchas= None,    
            sales= self,
            pur_qty= None,
            sale_qty= self.qty,
            total_bal_qty= totalBal
        )
    

class Inventory(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    purchas= models.ForeignKey(Purchas, on_delete=models.CASCADE, null=True)
    sales= models.ForeignKey(Sales, on_delete=models.CASCADE, null=True)
    pur_qty= models.FloatField(default=0, null=True)
    sale_qty= models.FloatField(default=0, null=True)
    total_bal_qty= models.FloatField()

    class Meta:
        verbose_name_plural='Inventory'

    def pur_date(self):
        if self.purchas:
            return self.purchas.pur_date
        
    def sales_date(self):
        if self.sales:
            return self.sales.sales_date
        