from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ForumForm
from .models import ForumPost


def forum_list_view(request):
    forum_posts = ForumPost.objects.all().order_by("-created_at")
    return render(request, "forum/list.html", {"forum_posts": forum_posts})


@login_required(login_url="users:login")
def forum_create_view(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("forum:detail", post_id=post.id)
    else:
        form = ForumForm()
    return render(request, "forum/create.html", {"form": form})


def forum_post_view(request, post_id):
    forum_post = ForumPost.objects.get(pk=post_id)
    return render(request, "forum/detail.html", {"forum_post": forum_post})
