from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib import messages

def events(request):
    events = Event.objects.all()
    return render(request, 'app1/events.html', {'events':events})

def add_event(request):
    if request.method == 'POST':
        event = Event()
        event.event_name = request.POST['ev_name']
        event.data = request.POST['data']
        event.location = request.POST['loc']
        event.image = request.FILES['img']
        event.save()
        messages.success(request, 'Event added successfully')
        return redirect('app1:events')
    return render(request, 'app1/add_event.html')


def event_fav(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.is_liked = not event.is_liked
    event.save()
    return redirect('app1:events')
