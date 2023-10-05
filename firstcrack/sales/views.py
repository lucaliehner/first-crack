from django.shortcuts import render
from .models import Sale
from django.views import generic
# Create your views here.

class SalesList(generic.ListView):
    model = Sale

