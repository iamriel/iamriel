from django.test import SimpleTestCase

from ..forms import ContactForm


class ContactFormTests(SimpleTestCase):

    def test_valid_data(self):
        data = {
            'email': 'me@iamriel.com',
            'subject': 'A Subject',
            'message': 'Just a Message',
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())
