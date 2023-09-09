from django.shortcuts import render
from . forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as blog_login
from django.shortcuts import redirect


def profile(request):
    pass


def login(request):

    login_form = LoginForm

    if request.method == "POST":

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data["username"]
            user = User.objects.get(username=username)

            blog_login(request, user)

            return redirect("main:home")

    return render(request, "account/login.html", {"login_form": login_form})


def register(request):

    return render(request, "account/register.html")

