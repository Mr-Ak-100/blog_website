from django.shortcuts import render, get_object_or_404, redirect
from . models import Article, Category, Comment
from . forms import CommentForm
from django.core.paginator import Paginator
from django.http import Http404
from log_system.base import LogSystem
from itertools import chain


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
    comment_form = CommentForm

    if request.method == "POST":

        comment_form = comment_form(request.POST)

        if comment_form.is_valid():

            Comment.objects.create(
                article=article,
                user=request.user,
                body=comment_form.cleaned_data["body"],
                published=True
            )

            return redirect("article:detail", article_slug)

        # else: show form error message in template

    comments = article.comments.published().order_by("-created")

    log = LogSystem(request, article)
    log.set_log()

    article.views = article.requests.count()
    article.save()

    return render(request, "article/detail.html", {"sidebar": True, "article": article, "comments": comments, "comment_form": comment_form})


def search(request):

    value = request.GET["value"]

    title_search = Article.objects.filter(title__icontains=value)
    body_search = Article.objects.filter(body__icontains=value)

    objects = sorted(chain(title_search, body_search))

    return render(request, "article/articles.html", {"sidebar": True, "articles": objects, "banner_name": f"جستجو برای {value}"})

