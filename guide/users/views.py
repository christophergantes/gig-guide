from django.contrib.auth import forms, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NameForm, ProfileForm
from .models import Profile


def register_view(request):
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = Profile()
            profile.user = user
            profile.save()
            return redirect("core:home")
    else:
        form = forms.UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return render(
        request, "users/profile_detail.html", {"profile": profile, "person": user}
    )


@login_required(login_url="users:login")
def profile_edit_view(request):
    user = request.user
    profile = user.profile
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        name_form = NameForm(request.POST, instance=user)
        if profile_form.is_valid() and name_form.is_valid():
            profile.bio = profile_form.cleaned_data.get("bio")
            if request.POST.get("picture-clear") == "on":
                profile.picture = "pfp/no_pfp.png"
            else:
                profile.picture = (
                    profile_form.cleaned_data.get("picture") or profile.picture
                )
            profile.save()
            name_form.save()
            return redirect("users:profile", username=request.user.username)
    else:
        profile_form = ProfileForm(instance=profile)
        name_form = NameForm(instance=user)
    return render(
        request,
        "users/profile_edit.html",
        {"name_form": name_form, "profile_form": profile_form},
    )


@login_required(login_url="users:login")
def settings_view(request):
    return render(request, "users/settings.html")
