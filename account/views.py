from django.shortcuts import render
from . forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login as blog_login
from django.contrib.auth import logout as blog_logout
from django.shortcuts import redirect


def profile(request):
    pass


def logout(request):

    blog_logout(request)
    return redirect("main:home")


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

    register_form = RegisterForm

    if request.method == "POST":

        register_form = register_form(request.POST)

        if register_form.is_valid():

            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]

            user = User(username=username, password=password)
            user.save()

            blog_login(request, user)
            return redirect("main:home")

    return render(request, "account/register.html", {"register_form": register_form})

