from sales.models import Sale, Product
from events.models import Event

def badges(request):
    open_sales = Sale.objects.exclude(status = "PAYED")
    all_events = Event.objects.all()
    all_products = Product.objects.all()

    context = {
            'open_sales' : open_sales,
            'all_events' : all_events,
            'all_products': all_products
            }
    return context
