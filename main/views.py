from django.http import HttpResponse
from django.template import RequestContext, loader


def coming_soon(request):
    template = loader.get_template('main/coming-soon.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))


def home(request):
    template = loader.get_template('main/base.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))

