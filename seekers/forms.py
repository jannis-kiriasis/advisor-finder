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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super(SeekerSignupForm, self).__init__(*args, **kwargs)

        self.fields['postcode'].widget.attrs['placeholder'] = 'Your postcode'
        self.fields['street_address'].widget.attrs['placeholder'] = 'Your street address'
        self.fields['need'].empty_label = 'What is the main area your are looking for advice on?'
        self.fields['town_or_city'].empty_label = 'Your location (town or city)'
        self.fields['need'].widget.attrs['class'] = 'text-muted'
        self.fields['town_or_city'].widget.attrs['class'] = 'text-muted'


class MessageForm(forms.ModelForm):
    """
    Create chat message form
    """
    class Meta:
        model = Message
        fields = ['body',]

        widgets = {
          'body': Textarea(attrs={'rows': 2, 'cols': 20}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs['placeholder'] = 'Send a message to your advisor'