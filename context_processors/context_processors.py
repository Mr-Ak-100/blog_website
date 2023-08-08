from home.models import Info, Social


def sidebar(request):
    return {"sidebar": False}


def main_info(request):

    info = Info.objects.first()
    social = Social.objects.first()

    return {"info": info, "social": social}
