from django.shortcuts import render
from .forms import ConsultationForm
from .models import Consultation
from matches.models import Match
from django.contrib import messages
from django.utils.crypto import get_random_string


def create_consultation(consultation_form, match, request):

    """
    Save consultation object in Consultation model
    """

    if consultation_form.is_valid():

        consultation_form.instance.match = match

        # Create meeting link with random string
        consultation_form.instance.link = 'https://gotalk.to/' + get_random_string(length=10)

        consultation_form.save()

        messages.success(
            request,
            'Consultation created. An email has been sent to your client.'
            )

    else:
        form = ConsultationForm(data=request.POST)

        messages.error(request, 'not valid')
