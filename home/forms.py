from .models import UserProfile
from django import forms


class UserTypeForm(forms.ModelForm):
    """
    Create an UserTypeForm.
    """
    class Meta:
        model = UserProfile
        fields = [
            'user_type',
        ]

