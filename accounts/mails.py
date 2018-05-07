from django.core.mail import EmailMessage


def notify_email(email_object):
        email = EmailMessage(
            email_object.subject,
            email_object.message,
            email_object.email,
            ['me@iamriel.com'],
        )
        email.send()
