from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Create order form for checkout view.
    """
    class Meta:
        """
        Define fields to show in form.
        """
        model = Order
        fields = [
            'name',
            'last_name',
            'email',
            'street_address',
            'town_or_city',
            'consultation',
            'seeker'
        ]

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
            'street_address': 'Address'

        }

        self.fields['name'].widget.attrs['autofocus'] = True

        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['street_address'].widget.attrs['placeholder'] = 'Address'

        self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
