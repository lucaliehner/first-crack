from django.shortcuts import render
from .models import Sale, ProductVariation
from django.views import generic
# Create your views here.

class SalesList(generic.ListView):
    model = Sale

class SaleDetail(generic.DetailView):
    model = Sale

class ProductList(generic.ListView):
    model = ProductVariation
