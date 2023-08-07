from django.shortcuts import render
from . forms import MessageForm
from . models import Message


def home(request):
    return render(request, "home/index.html", {"sidebar": True})


def about(request):
    return render(request, "home/about.html", {"sidebar": True})


def contact(request):

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(data=request.POST)

        if form.is_valid():

            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")

            Message.objects.create(name=name, email=email, title=title, body=body)

    return render(request, "home/contact.html", {"form": form})
