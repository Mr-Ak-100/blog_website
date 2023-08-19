from django.shortcuts import render, get_object_or_404
from . models import Article, Category, ArticleView, Comment
from django.core.paginator import Paginator
from django.http import Http404
from log_system.base import LogSystem


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

    log = LogSystem(request)
    log.set_log()

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

    log = LogSystem(request, page=f"category/{category_slug}")
    log.set_log()

    return render(request, "article/articles.html", {"sidebar": True, "articles": objects, "banner_name": banner_name})


def detail(request, article_slug):

    article = get_object_or_404(Article, slug=article_slug)
    comments = article.comments.published().order_by("-created")

    log = LogSystem(request, article)
    log.set_log()

    article.views = article.requests.count()
    article.save()

    return render(request, "article/detail.html", {"sidebar": True, "article": article, "comments": comments})
