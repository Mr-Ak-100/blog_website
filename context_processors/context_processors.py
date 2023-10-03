from home.models import Info, Social
from article.models import Category, Article


def sidebar(request):

    sidebar_categories = Category.objects.sidebar_items()
    sidebar_most_view = Article.objects.published().order_by("-views")[:3]

    return {"sidebar": False, "sidebar_categories": sidebar_categories, "sidebar_most_view": sidebar_most_view}


def main_info(request):

    info = Info.objects.first()
    social = Social.objects.first()

    return {"info": info, "social": social}
