from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdvisorSignupForm, MessageForm
from .models import AdvisorUserProfile, User
from .emails import advisor_to_approve_email, advisor_deactivated_email, advisor_activated_email, email_note_to_seeker
from matches.models import Match, Message
from consultations.views import create_consultation
from consultations.forms import ConsultationForm
from consultations.models import Consultation
from itertools import chain


@login_required
def advisor_signup(request):

    """
    View to let an advisor signup. Takes the form it is valid
    and if so save the objects in the related models.

    If the advisor profile is created, send a feedback.
    """

    if request.method == 'POST':
        form = AdvisorSignupForm(request.POST)

        if form.is_valid():

            form.instance.user = request.user
            form.save()

            messages.success(
                request,
                'Signup completed. Now wait for Advice Found profile check.'
                )

            queryset = AdvisorUserProfile.objects
            profile = get_object_or_404(queryset, user=request.user)

            advisor_to_approve_email(profile)

            return redirect('advisor_signup')

        else:
            messages.error(request, 'Signup not completed. Try again.')

    form = AdvisorSignupForm()

    context = {
        'form': form,
        'page_title': 'Financial Advisor Signup'
    }
    return render(request, 'advisors/signup.html', context)


@login_required
def advisor_profile(request):

    """
    advisor_profile view for profile.html.
    Render all the business details related to an advisor.
    """

    user = request.user
    queryset = AdvisorUserProfile.objects
    profile = get_object_or_404(queryset, user=user)

    form = AdvisorSignupForm(instance=profile)

    if request.method == 'POST':

        form = AdvisorSignupForm(request.POST, instance=profile)

        if form.is_valid():

            profile.approved = 0
            profile = form.save()

            messages.success(
                request,
                'Your update request has been forwarded. Now wait for Advice Found review.'
            )

            advisor_to_approve_email(profile)

            return redirect('advisor_profile')

        else:

            messages.error(
                request,
                "Your update request didn't go through. Try again."
            )

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.business_name} profile'
    }

    return render(request, 'advisors/profile.html', context)


@login_required
def deactivate_profile(request):
    """
    View to deactivate profile.
    If profile is deactivated / activated, send a feedback.
    """

    user = request.user
    profile = get_object_or_404(AdvisorUserProfile, user=user)

    if profile.active == 1:

        profile.active = 0
        profile.save()

        advisor_deactivated_email(user, profile)

        messages.success(request, 'Your profile has been deactivated.')

    else:

        profile.active = 1
        profile.save()

        advisor_activated_email(user, profile)

        messages.success(request, 'Your profile has been activated.')

    return redirect('advisor_profile')


@login_required
def matches_list(request):

    """
    View to show all of an advisor matches.
    """

    # # Get advisor profile of logged in user

    user = request.user
    advisor_objects = AdvisorUserProfile.objects
    advisor = get_object_or_404(advisor_objects, user=user)

    # Filter matches by logged in advisor

    matches = Match.objects.filter(advisor=advisor, is_client=False)

    context = {
        'matches': matches,
        'page_title': 'My Matches'
    }

    return render(request, 'advisors/matches.html', context)


@login_required
def clients_list(request):

    """
    View to show all of an advisor clients.
    """

    # # Get advisor profile of logged in user

    user = request.user
    advisor_objects = AdvisorUserProfile.objects
    advisor = get_object_or_404(advisor_objects, user=user)

    # Filter matches by logged in advisor

    matches = Match.objects.filter(advisor=advisor, is_client=True)

    context = {
        'matches': matches,
        'page_title': 'My Clients'
    }

    return render(request, 'advisors/clients.html', context)


@login_required
def seeker_profile(request, match_id):

    """
    Show the seekers details together with their messages.
    Show the consultation form and the message form.
    """

    # Get seeker details

    match = get_object_or_404(Match, id=match_id)

    notes = Message.objects.filter(match=match)

    consultations = Consultation.objects.filter(match=match)

    # Combine notes and consultations in 1 iterable list for template

    elements = list(chain(notes, consultations))

    if request.method == 'POST':

        if 'consultation' not in request.POST:
            message_form = MessageForm(data=request.POST)

            # If message form is valid get user id and save

            if message_form.is_valid():

                user = request.user
                message_form.instance.match = match
                message_form.instance.user = request.user

                message_form.save()

                messages.success(request, 'You have sent a message successfully. Your client will receive an email.')

                # Email last message to advisor

                # Get all messages by logged in user
                messages_sent = Message.objects.filter(user=user)

                # Get last message for logged in user by created_on and send
                last_message = messages_sent.latest('created_on')
                email_note_to_seeker(last_message)

            else:
                message_form = MessageForm()

            return reditect('seeker_profile')

        elif 'consultation' in request.POST:

            consultation_form = ConsultationForm(data=request.POST)

            create_consultation(consultation_form, match, request)

            return redirect('seeker_profile')

    context = {
        'match': match,
        'notes': notes,
        'consultations': consultations,
        'message_form': MessageForm,
        'consultation_form': ConsultationForm,
        'page_title': f'{ match }',
        'elements': elements
        }

    return render(request, 'advisors/client-profile.html', context)


@login_required
def consultation_list(request):

    """
    """ 

    get_advisor_profile = get_object_or_404(AdvisorUserProfile, user=request.user)

    get_all_matches = Match.objects.filter(advisor=get_advisor_profile)

    consultations = Consultation.objects.filter(
        match__id__in=get_all_matches
        ).order_by(
            '-date'
        )

    context = {
        'consultations': consultations,
        'page_title': 'Your appointments'
    }

    return render(request, 'advisors/appointments.html', context)


@login_required
def delete_consultation(request, consultation_id):

    """
    Delete consultation and show message.
    """

    consultation = get_object_or_404(Consultation, id=consultation_id)
    consultation.delete()
    messages.success(request, 'The consultation has been deleted.')

    return redirect('consultations')
