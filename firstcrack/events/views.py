from django.shortcuts import render
from django.views import generic
from .models import Event
# Create your views here.
class EventsList(generic.ListView):
    model = Event

def calendar(request):
    events = Event.objects.all()

    context = {
            'events': events
            }
    return render(request, 'events/calendar.html', context)

