from django.test import TestCase

from home.models import Location

from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Tests for order form.
    """
    def test_required_fields_are_required(self):
        """
        Test that all required fields are required.
        """
        form = OrderForm(
            {
                'name': '',
                'last_name': '',
                'email': '',
                'street_address': '',
                'town_or_city': '',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('street_address', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')
        self.assertEqual(
            form.errors['street_address'][0], 'This field is required.')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_not_required_fields(self):
        """
        Test that all the not required fields are not required.
        """
        form = OrderForm({
            'name': 'test',
            'last_name': 'test',
            'email': 'ciao@ciao.com',
            'street_address': 'fff',
            'town_or_city': Location.objects.create(city='Dublin')
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, [
            'name',
            'last_name',
            'email',
            'street_address',
            'town_or_city',
            'consultation',
            'seeker'
            ]
        )
