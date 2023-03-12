from django.test import TestCase

from home.models import Location, Specialisation

from .forms import UserTypeForm, CustomSignupForm


class TestUserTypeForm(TestCase):
    """
    Tests for user type form
    """
    def test_required_fields_is_required(self):
        """
        Test that all required fields are required.
        """
        form = UserTypeForm(
            {
                'user_type': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('user_type', form.errors.keys())

        self.assertEqual(
            form.errors['user_type'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = UserTypeForm()
        self.assertEqual(form.Meta.fields, [
            'user_type',
        ])


class TestCustomSignuoForm(TestCase):
    """
    Tests for custom signup form
    """
    def test_required_fields_is_required(self):
        """
        Test that all required fields are required.
        """
        form = CustomSignupForm(
            {
                'first_name': '',
                'last_name': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())

        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.')
