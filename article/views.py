from django.shortcuts import render, get_object_or_404
from . models import Article, Category
from django.core.paginator import Paginator
from django.http import Http404


def articles(request):

    banner_name = "پست ها"

    try:

        page = request.GET.get("page")
        if page:
            int(page)

    except ValueError:
        raise Http404()

    paginator = Paginator(Article.objects.published().order_by("-created"), 6)
    objects = paginator.get_page(page)

    return render(request, "article/articles.html", {"sidebar": True, "articles": objects, "banner_name": banner_name})


def category(request, category_slug):

    category_object = get_object_or_404(Category, slug=category_slug)
    banner_name = category_object.title

    try:

        page = request.GET.get("page")
        if page:
            int(page)

    except ValueError:
        raise Http404()

    paginator = Paginator(category_object.article_set.published().order_by("-created"), 6)
    objects = paginator.get_page(page)

    return render(request, "article/articles.html", {"sidebar": True, "articles": objects, "banner_name": banner_name})
