from django.test import TestCase

from .forms import ConsultationForm


class TestConsultationForm(TestCase):
    """
    Tests for consultation form.
    """
    def test_required_fields_are_required(self):
        """
        Test that all required fields are required.
        """
        form = ConsultationForm(
            {
                'date': '',
                'time': '',
                'price': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertIn('time', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['date'][0], 'This field is required.')
        self.assertEqual(
            form.errors['time'][0], 'This field is required.')
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that fields are explicit in form metaclass.
        """
        form = ConsultationForm()
        self.assertEqual(form.Meta.fields, ['date', 'time', 'price',])
