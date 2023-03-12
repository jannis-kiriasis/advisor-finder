from django.test import TestCase

from home.models import Location, Specialisation

from .forms import SeekerSignupForm, MessageForm


class TestSeekerSignupForm(TestCase):
    """
    Tests for seeker signup form.
    """
    def test_required_fields_is_required(self):
        """
        Test that all required fields are required.
        """
        form = SeekerSignupForm(
            {
                'need': '',
                'town_or_city': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('need', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())

        self.assertEqual(
            form.errors['need'][0], 'This field is required.')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_not_required_fields(self):
        """
        Test that all the not required fields are not required.
        """
        form = SeekerSignupForm({
            'need': Specialisation.objects.create(type='pensions'),
            'town_or_city': Location.objects.create(city='Dublin')
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = SeekerSignupForm()
        self.assertEqual(form.Meta.fields, [
            'need',
            'postcode',
            'town_or_city',
            'street_address',
        ])


class TestMessageForm(TestCase):
    """
    Tests for message form.
    """
    def test_required_fields_is_required(self):
        """
        Test that all required fields are required.
        """
        form = MessageForm(
            {
                'body': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())

        self.assertEqual(
            form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = MessageForm()
        self.assertEqual(form.Meta.fields, [
            'body',
        ])
