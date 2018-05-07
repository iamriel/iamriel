from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['active_user'] = User.objects.get(username=settings.ACTIVE_USERNAME)
        return context
