from django.urls import path

from . import views

app_name = "comments"

urlpatterns = [
    path("post/<int:post_id>", views.comment_create_view, name="post"),
    path("reply/<int:comment_id>", views.reply_create_view, name="reply"),
]
