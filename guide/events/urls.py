from django.urls import path
from . import views


app_name = "events"

urlpatterns = [
    path("", views.list_view, name="list"),
    path("create/", views.create_view, name="create"),
    path("post/<int:post_id>", views.post_view, name="post"),
]
