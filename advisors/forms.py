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

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super(AdvisorSignupForm, self).__init__(*args, **kwargs)

        placeholders = {
            'business_name': 'Business name',
            'business_description': 'Business description',
            'specialisation': 'Specialisation',
            'postcode': 'Your postcode',
            'street_address': 'Business address',
            'town_or_city': 'Town or city',
            'registration_number': 'Registration number'
        }

        self.fields['business_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
        self.fields[
            'specialisation'].empty_label = 'What do you specialise in? *'
        self.fields[
            'town_or_city'].empty_label = 'Your business location *'


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

        self.fields['body'].widget.attrs[
                'placeholder'] = 'Send a message to your client'
