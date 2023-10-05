from django.db import models
from address.models import AddressField
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ProductVariation(models.Model):
    specification = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    retail_price = models.DecimalField(decimal_places=2, max_digits=10)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.product.name + " | " + self.specification 


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = AddressField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sale(models.Model):

    NEW = 'New order'
    ACCEPTED = 'Accepted'
    DECLINED = 'Declined'
    PROCESSED = 'In process'
    DELIVRERD = 'Deliverd to customer'
    INVOICED = 'Invoice sent'
    PAYED = 'Invoice payed'

    STATUS = [
            (NEW, 'New order'),
            (ACCEPTED, 'Accepted'),
            (DECLINED, 'Declined'),
            (PROCESSED, 'In process'),
            (DELIVRERD, 'Delivered to customer'),
            (INVOICED, 'Invoice sent'),
            (PAYED, 'Invoice payed')
            ]
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
            max_length = 255, 
            verbose_name = "State of the current order",
            choices = STATUS,
            default = NEW
            )
    delivery_date = models.DateField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    purchases = models.ManyToManyField(ProductVariation, through="Purchase")
    def __str__(self):
        return str(self.id)

class Purchase(models.Model):
    quantity = models.IntegerField()
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)


