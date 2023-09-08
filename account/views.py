from django.shortcuts import render


def profile(request):
    pass


def login(request):

    return render(request, "account/login.html")
