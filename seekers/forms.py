from .models import SeekerUserProfile
from django import forms
from django.forms import Textarea
from matches.models import Message


class SeekerSignupForm(forms.ModelForm):

    """
    Create an Seekers Signup form.
    """

    class Meta:
        model = SeekerUserProfile
        fields = [
            'need',
            'postcode',
            'town_or_city',
            'street_address',
        ]


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
