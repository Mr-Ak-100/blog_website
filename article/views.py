from django.shortcuts import render, get_object_or_404
from . models import Article, Category, ArticleView, Comment
from django.core.paginator import Paginator
from django.http import Http404
from django_user_agents.utils import get_user_agent


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


def detail(request, article_slug):

    article = get_object_or_404(Article, slug=article_slug)
    comments = article.comments.published().order_by("-created")
    user_agents = get_user_agent(request)

    def get_client_ip():

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_client_device():

        if user_agents.is_mobile is True:
            device = "Mobile"
        elif user_agents.is_pc is True:
            device = "Pc"
        elif user_agents.is_tablet is True:
            device = "Tablet"

        return device

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    ArticleView.objects.create(
        article=article,
        user=user,
        client_ip=get_client_ip(),
        device=get_client_device(),
        os=user_agents.os.family,
        os_version=user_agents.os.version_string,
        browser=user_agents.browser.family,
        browser_version=user_agents.browser.version_string
    )

    article.views = article.requests.count()
    article.save()

    return render(request, "article/detail.html", {"sidebar": True, "article": article, "comments": comments})
