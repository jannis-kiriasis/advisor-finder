from .models import AdvisorUserProfile
from django import forms
from django.forms import Textarea
from matches.models import Message


class AdvisorSignupForm(forms.ModelForm):
    """
    Create an Advisor Signup form.
    """
    class Meta:
        model = AdvisorUserProfile
        fields = [
            'business_name',
            'business_description',
            'specialisation',
            'postcode',
            'town_or_city',
            'street_address',
            'registration_number',
        ]

        widgets = {
            'business_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }


class MessageForm(forms.ModelForm):

    """
    Create chat message form
    """

    class Meta:
        model = Message
        fields = ['body',]

        widgets = {
          'body': Textarea(attrs={'rows': 2, 'cols':20}),
        }
