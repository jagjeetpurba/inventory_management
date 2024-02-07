from django import forms
from .models import *
from django.forms import ModelForm


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        self.staff = kwargs.pop('staff')
        super().__init__(*args, **kwargs)
        self.fields['staff'].initial = self.staff
        self.fields['staff'].widget = forms.HiddenInput()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.staff = self.staff
        if commit:
            instance.save()
        return instance

'''
        widgets={
            'customer': forms.ChoiceField(attrs={'class': 'form-control'}),
            'product': forms.ChoiceField(attrs={'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'staff': forms.ChoiceField(attrs={'class': 'form-control'}),
        }


#class PurchaseForm(forms.ModelForm):



class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields= '__all__'

class PurchaseForm(forms.Form):
    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    quant = forms.IntegerField()

class SaleForm(forms.Form):
    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    quant = forms.IntegerField()

'''