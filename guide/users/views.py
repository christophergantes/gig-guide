from django.contrib.auth import forms, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm
from .models import Profile


def register_view(request):
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            profile = Profile()
            profile.user = request.user
            profile.save()
            return redirect("core:home")
    else:
        form = forms.UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect("core:home")

    else:
        form = forms.AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("core:home")
    return redirect("core:home")


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return render(
        request, "users/profile_detail.html", {"profile": profile, "person": user}
    )


@login_required(login_url="users:login")
def edit_profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.bio = form.cleaned_data.get("bio")
            if request.POST.get("picture-clear") == "on":
                profile.picture = "pfp/no_pfp.png"
            else:
                profile.picture = form.cleaned_data.get("picture") or profile.picture
            profile.save()
            return redirect("users:profile", username=request.user.username)
    else:
        form = ProfileForm(initial={"bio": profile.bio, "picture": profile.picture})
    return render(request, "users/profile_edit.html", {"form": form})
