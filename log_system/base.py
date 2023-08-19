from django_user_agents.utils import get_user_agent
from home.models import Log as HomeLog
from article.models import ArticleView


class LogSystem:

    def __init__(self, request, article=None, page=None):

        self.request = request
        self.article = article
        self.user_agents = get_user_agent(request)
        self.user = None
        self.page = page

        if page is None:
            self.page = self.request.resolver_match.url_name

        if request.user.is_authenticated:
            self.user = self.request.user

    def get_client_ip(self):

        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        return ip

    def get_client_device(self):

        if self.user_agents.is_mobile is True:
            device = "Mobile"
        elif self.user_agents.is_pc is True:
            device = "Pc"
        elif self.user_agents.is_tablet is True:
            device = "Tablet"

        return device

    def set_log(self):

        if self.article:

            ArticleView.objects.create(
                article=self.article,
                user=self.user,
                client_ip=self.get_client_ip(),
                device=self.get_client_device(),
                os=self.user_agents.os.family,
                os_version=self.user_agents.os.version_string,
                browser=self.user_agents.browser.family,
                browser_version=self.user_agents.browser.version_string
            )

        else:

            HomeLog.objects.create(
                page=self.page,
                user=self.user,
                client_ip=self.get_client_ip(),
                device=self.get_client_device(),
                os=self.user_agents.os.family,
                os_version=self.user_agents.os.version_string,
                browser=self.user_agents.browser.family,
                browser_version=self.user_agents.browser.version_string
            )
