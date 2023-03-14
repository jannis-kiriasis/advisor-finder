from .models import AdvisorUserProfile
from django import forms
from django.forms import Textarea
from matches.models import Message


class AdvisorSignupForm(forms.ModelForm):
    """
    Create an Advisor Signup form.
    """
    class Meta:
        """
        Define fields to show in form.
        """
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
        Add placeholdersadn empty labels. Remove auto-generated
        labels and set autofocus on first field
        """
        super(AdvisorSignupForm, self).__init__(*args, **kwargs)

        self.fields['business_name'].widget.attrs['autofocus'] = True
        self.fields['business_name'].widget.attrs[
            'placeholder'] = 'Business name *'
        self.fields['business_description'].widget.attrs[
            'placeholder'] = 'Business description *'
        self.fields['postcode'].widget.attrs[
            'placeholder'] = 'Your postcode'
        self.fields['street_address'].widget.attrs[
            'placeholder'] = 'Business address *'
        self.fields['registration_number'].widget.attrs[
            'placeholder'] = 'Registration number *'

        for field in self.fields:
            self.fields[field].label = False

        self.fields[
            'specialisation'].empty_label = 'What do you specialise in? *'
        self.fields[
            'town_or_city'].empty_label = 'Your business location *'


class MessageForm(forms.ModelForm):
    """
    Create chat message form.
    """
    class Meta:
        """
        Define fields to show in form.
        """
        model = Message
        fields = ['body', ]

        widgets = {
          'body': Textarea(attrs={'rows': 2, 'cols': 20}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders to body field.
        """
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs[
                'placeholder'] = 'Send a message to your client'
