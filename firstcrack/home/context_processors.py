from sales.models import Sale
from events.models import Event

def badges(request):
    open_sales = Sale.objects.exclude(status = "PAYED")
    all_events = Event.objects.all()

    context = {
            'open_sales' : open_sales,
            'all_events' : all_events
            }
    return context
