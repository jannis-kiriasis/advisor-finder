from .models import SeekerUserProfile
from django import forms
from django.forms import Textarea


class SeekerSignupForm(forms.ModelForm):
    """
    Create an Seekers Signup form.
    """
    class Meta:
        model = SeekerUserProfile
        fields = [
            'user',
            'need',
            'postcode',
            'town_or_city',
            'street_address',
        ]
