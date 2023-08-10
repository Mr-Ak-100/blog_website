from django.shortcuts import render
from . models import Article
from django.core.paginator import Paginator


def articles(request):

    banner_name = "پست ها"

    page = request.GET.get("page")
    if page:
        int(page)

    paginator = Paginator(Article.objects.published(), 6)
    objects = paginator.get_page(page)

    return render(request, "article/articles.html", {"sidebar": True, "articles": objects, "banner_name": banner_name})
