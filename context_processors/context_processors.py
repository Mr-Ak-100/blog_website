from home.models import Info, Social
from article.models import Category


def sidebar(request):

    sidebar_categories = Category.objects.sidebar_items()

    return {"sidebar": False, "sidebar_categories": sidebar_categories}


def main_info(request):

    info = Info.objects.first()
    social = Social.objects.first()

    return {"info": info, "social": social}
