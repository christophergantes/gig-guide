from core.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .forms import CommentForm
from .models import Comment

# Create your views here.


@login_required(login_url="users:login")
def comment_create_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    if post.is_event():
        return redirect("events:detail", post_id=post_id)
    return redirect("forum:detail", post_id=post_id)


@login_required(login_url="users:login")
def reply_create_view(request, comment_id):
    parent = get_object_or_404(Comment, id=comment_id)
    post = parent.post

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent = parent
            reply.post = post
            reply.save()

    if post.is_event():
        return redirect("events:detail", post_id=post.id)
    return redirect("forum:detail", post_id=post.id)
