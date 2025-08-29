from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("account/register/", views.register_view, name="register"),
    path("account/login/", views.login_view, name="login"),
    path("account/logout/", views.logout_view, name="logout"),
    path("account/", views.account_view, name="account"),
    path("account/edit", views.account_edit_view, name="account-edit"),
    path(
        "account/password-change/", views.password_change_view, name="password-change"
    ),
    path(
        "account/password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/password_reset_email.html",
            success_url="/users/account/password-reset-done",
        ),
        name="password-reset",
    ),
    path(
        "account/password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "account/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url="/users/account/reset/done",
        ),
        name="password-reset-confirm",
    ),
    path(
        "account/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password-reset-complete",
    ),
    path("profile/edit/", views.edit_profile_view, name="edit-profile"),
    path("<str:username>/", views.profile_view, name="profile"),
]
