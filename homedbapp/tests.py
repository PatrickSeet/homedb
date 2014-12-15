from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from homedbapp.forms import EmailUserCreationForm
from homedbapp.models import Shopper


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        Shopper.objects.create_user(username='test-user')

        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        with self.assertRaises(ValidationError):
            form.clean_username()