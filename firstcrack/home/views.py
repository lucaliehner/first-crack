from django.shortcuts import render
from events.models import Event

# Create your views here.
def index(request):
    events = Event.objects.all()

    context = {
            'events': events
            }
    return render(request, 'home/index.html', context)
