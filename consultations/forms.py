from django import forms
from .models import Consultation
from django.forms import widgets


class ConsultationForm(forms.ModelForm):

    """
    Create a consultation.
    """

    class Meta:
        model = Consultation

        fields = ['date', 'time', 'price',]

        labels = {
            'date': 'Consultation date',
            'time': 'Consultation time',
            'price': 'Consultation fee in €'
        }

        widgets = {
            'date': widgets.DateInput(
                attrs={'type': 'date'}
            ),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
