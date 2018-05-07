from django import forms
from django.core.mail import EmailMessage

from .models import Email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

    def send_notification(self):
        data = self.validated_data
        email = EmailMessage(
            data['subject'],
            data['message'],
            data['email'],
            ['me@iamriel.com'],
        )
        email.send()
