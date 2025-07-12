from django.shortcuts import render, redirect
from django.contrib.auth import forms
from django.contrib.auth import login, logout


def register_view(request):
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home")
    else:
        form = forms.UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")

    else:
        form = forms.AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return redirect("home")
