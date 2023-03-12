from django.test import TestCase

from home.models import Location, Specialisation

from .forms import AdvisorSignupForm


class TestAdvisorSignupForm(TestCase):
    """
    Tests for advisor signup form
    """
    def test_required_fields_is_required(self):
        """
        Test that all required fields are required.
        """
        form = AdvisorSignupForm(
            {
                'business_name': '',
                'business_description': '',
                'specialisation': '',
                'town_or_city': '',
                'registration_number': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('business_name', form.errors.keys())
        self.assertIn('business_description', form.errors.keys())
        self.assertIn('specialisation', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('registration_number', form.errors.keys())
        self.assertEqual(
            form.errors['business_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['business_description'][0], 'This field is required.')
        self.assertEqual(
            form.errors['specialisation'][0], 'This field is required.')
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')
        self.assertEqual(
            form.errors['registration_number'][0], 'This field is required.')

    def test_not_required_fields(self):
        """
        Test that all the not required fields are not required.
        """
        form = AdvisorSignupForm({
            'business_name': 'test',
            'business_description': 'test',
            'specialisation': Specialisation.objects.create(type='pensions'),
            'town_or_city': Location.objects.create(city='Dublin'),
            'registration_number': '777777',
            'street_address': 'fff',
            'postcode': ''
            }
        )
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = AdvisorSignupForm()
        self.assertEqual(form.Meta.fields, [
            'business_name',
            'business_description',
            'specialisation',
            'postcode',
            'town_or_city',
            'street_address',
            'registration_number',
        ])
