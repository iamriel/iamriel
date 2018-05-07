from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .mails import notify_email
from .models import Email


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        notify_email(self.object)
        if self.request.is_ajax():
            data = {
                'message': 'Thank you for your message.  I will get back to you as soon as I can.',
            }
            return JsonResponse(data)
        else:
            return response


class ContactFormView(AjaxableResponseMixin, CreateView):
    model = Email
    fields = ['email', 'subject', 'message']
    success_url = '/'
