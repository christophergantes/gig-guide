from django.urls import path

from . import views

app_name = "forum"

urlpatterns = [
    path("", views.forum_list_view, name="list"),
    path("create/", views.forum_create_view, name="create"),
    path("post/<int:post_id>/", views.forum_post_view, name="detail"),
]
