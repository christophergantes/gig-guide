from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import EventForm
from .models import EventPost


def list_view(request):
    events = EventPost.objects.all().order_by("-created_at")
    return render(request, "events/list.html", {"events": events})


@login_required(login_url="users:login")
def create_view(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect("events:detail", post_id=event.id)
    return render(request, "events/create.html")


def event_post_view(request, post_id):
    event = EventPost.objects.get(pk=post_id)
    comments = event.comments.filter(parent__isnull=True)
    return render(request, "events/detail.html", {"event": event, "comments": comments})
