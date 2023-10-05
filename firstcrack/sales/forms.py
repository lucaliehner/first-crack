from django import forms
from .models import Sale, Purchase

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['client', 'delivery_date']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity']


