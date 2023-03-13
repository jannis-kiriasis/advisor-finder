from django import forms
from .models import Consultation
from django.forms import widgets


class ConsultationForm(forms.ModelForm):
    """
    Create a consultation form.
    """
    class Meta:
        """
        Define fields to show in form.
        """
        model = Consultation

        fields = ['date', 'time', 'price',]

        widgets = {
            'date': widgets.DateInput(
                attrs={'type': 'date'}
            ),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders to fields and remove labels
        """
        super(ConsultationForm, self).__init__(*args, **kwargs)

        placeholders = {
            'price': 'Consultation fee in €'
        }

        for field in self.fields:
            self.fields[field].label = False

        self.fields['price'].widget.attrs[
            'placeholder'] = 'Consultation fee in € *'
