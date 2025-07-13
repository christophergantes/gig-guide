from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def list_view(request):
    events = Event.objects.all().order_by("-created_at")
    return render(request, "events/list.html", {"events": events})


@login_required(login_url="users:login")
def create_view(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            # change to redirect to post page
            return redirect("events:list")
    else:
        form = EventForm()

    return render(request, "events/create.html", {"form": form})
