from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'name',
            'last_name',
            'email',
            'phone_number',
            'street_address',
            'town_or_city',
            'consultation',
            'seeker'
        )

        widgets = {
            'consultation': forms.HiddenInput(),
            'seeker': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):

        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Address',
            'town_or_city': 'Town or city',
            'consultation': 'Consultation',
            'seeker': 'Seeker'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
