from django.shortcuts import render, get_object_or_404
from .forms import ConsultationForm
from .models import Consultation
from matches.models import Match
from django.contrib import messages
from django.utils.crypto import get_random_string
from .emails import email_consultation_seeker


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

        consultation = Consultation.objects.filter(match=match).latest('match')

        # email_consultation_seeker(consultation)

    else:
        form = ConsultationForm(data=request.POST)

        messages.error(request, 'not valid')
