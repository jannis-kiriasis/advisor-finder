from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):

    """
    Create a consultation.
    """

    class Meta:
        model = Consultation
        fields = ['date', 'time', 'link', 'price',]
