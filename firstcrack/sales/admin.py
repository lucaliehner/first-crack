from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Sale, Client, ProductVariation, Purchase

# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass


class SalesInline(admin.TabularInline):
    model = Sale.purchases.through
@admin.register(Sale)
class SaleAdmin(ImportExportModelAdmin):
    inlines = [SalesInline]
@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    pass

@admin.register(ProductVariation)
class ProductVariationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseAdmin(ImportExportModelAdmin):
    pass


