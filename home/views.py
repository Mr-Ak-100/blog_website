from django.shortcuts import render


def home(request):
    return render(request, "home/index.html", {"sidebar": True})


def about(request):
    return render(request, "home/about.html", {"sidebar": True})


def contact(request):
    return render(request, "home/contact.html")
