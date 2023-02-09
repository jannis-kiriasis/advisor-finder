from .models import AdvisorUserProfile
from django import forms
from django.forms import Textarea


class AdvisorSignupForm(forms.ModelForm):
    """
    Create an Advisor Signup form.
    """
    class Meta:
        model = AdvisorUserProfile
        fields = [
            'user',
            'business_name',
            'business_description',
            'specialisation',
            'postcode',
            'town_or_city',
            'street_address',
        ]
        widgets = {
            'business_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
