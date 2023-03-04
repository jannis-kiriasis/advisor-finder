from .models import UserProfile
from django import forms
from allauth.account.forms import SignupForm


class UserTypeForm(forms.ModelForm):
    """
    Create an UserTypeForm.
    """
    class Meta:
        model = UserProfile
        fields = [
            'user_type',
        ]


# Custom signup form

class CustomSignupForm(SignupForm):
    """
    Customise the signup form.
    Add first_name, last_name.
    Validate and save the new fields.
    """

    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    phone_number = forms.CharField(max_length=20, label='phone_number')

    def signup(self, request, user):

        """Validate new fields and save"""

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
