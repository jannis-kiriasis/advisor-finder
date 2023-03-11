from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from matches.models import Match

from .forms import ConsultationForm
from .models import Consultation
from .emails import email_consultation_seeker


def confirm_consultation(order):
    get_consultation = order.consultation

    get_consultation.status = 1
    get_consultation.save()


def create_consultation(consultation_form, match, request):
    """
    Save consultation object in Consultation model
    """
    if consultation_form.is_valid():

        consultation_form.instance.match = match
        consultation_form.save()
        messages.success(
            request,
            'Consultation created. An email has been sent to your client.'
            )

        consultation = Consultation.objects.filter(
            match=match
            ).latest(
                'created'
            )

        email_consultation_seeker(consultation)

    else:
        form = ConsultationForm(data=request.POST)

        messages.error(request, 'Form not valid.')
