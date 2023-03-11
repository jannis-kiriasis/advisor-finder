from django import forms
from .models import Consultation
from django.forms import widgets


class ConsultationForm(forms.ModelForm):
    """
    Create a consultation form.
    """
    class Meta:
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
            'date': 'Consultation date',
            'time': 'Consultation time',
            'price': 'Consultation fee in €'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
