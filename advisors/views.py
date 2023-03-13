from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from advisor_finder.utils import get_advisor_by_request_user
from matches.models import Match, Message
from consultations.utils import create_consultation
from consultations.forms import ConsultationForm
from consultations.models import Consultation
from home.models import Specialisation, Location

from .forms import AdvisorSignupForm, MessageForm
from .models import AdvisorUserProfile
from .emails import advisor_to_approve_email, advisor_deactivated_email
from .emails import advisor_activated_email, email_note_to_seeker
from .emails import consultation_cancelled
from .utils import profile_status_messasge
from .utils import save_advisor_updates_in_request_session
from .utils import find_uncorfirmed_consultation


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

            profile = get_advisor_by_request_user(request)

            advisor_to_approve_email(profile)

            return redirect('advisor_profile')

            messages.success(
                request,
                'Signup completed. Now wait for Advice Found profile check.'
                )

        else:
            messages.error(request, 'Signup not completed. Try again.')

    form = AdvisorSignupForm()

    context = {
        'form': form
    }

    return render(request, 'advisors/signup.html', context)


@login_required
def advisor_profile(request):
    """
    advisor_profile view for profile.html.
    Render all the business details related to an advisor.
    """
    profile = get_advisor_by_request_user(request)

    form = AdvisorSignupForm(instance=profile)

    profile_status_messasge(request, profile)

    if request.method == 'POST':

        form = AdvisorSignupForm(request.POST, instance=profile)

        if form.is_valid():

            # Save POST data in request session to pass to the update_advisor
            # view after defensive design
            save_advisor_updates_in_request_session(request)

            return redirect(reverse(
                'update_advisor',
            ))

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.business_name} profile'
    }

    return render(request, 'advisors/profile.html', context)


@login_required
def update_advisor(request):
    """
    advisor_profile view for profile.html.
    """
    saved_specialisation = request.POST['save_specialisation']
    saved_business_name = request.POST['save_business_name']
    saved_business_description = request.POST['save_business_description']
    saved_registration_number = request.POST['save_registration_number']
    saved_postcode = request.POST['save_postcode']
    saved_street_address = request.POST['save_street_address']
    saved_town_or_city = request.POST['save_town_or_city']

    specialisation = get_object_or_404(
        Specialisation,
        type=saved_specialisation
    )

    town_or_city = Location.objects.filter(
        city=saved_town_or_city
    ).latest('city')

    profile = get_advisor_by_request_user(request)

    print(saved_registration_number)
    profile.specialisation = specialisation
    profile.business_name = saved_business_name
    profile.business_description = saved_business_description
    profile.registration_number = saved_registration_number
    profile.postcode = saved_postcode
    profile.street_address = saved_street_address
    profile.town_or_city = town_or_city
    profile.approved = 0

    new_profile = profile.save()
    profile = new_profile
    advisor_to_approve_email(profile)

    del request.session['save_specialisation']
    del request.session['save_business_name']
    del request.session['save_business_description']
    del request.session['save_registration_number']
    del request.session['save_postcode']
    del request.session['save_street_address']
    del request.session['save_town_or_city']

    messages.success(request, 'Your edits have been forwarded for approval.')

    return redirect(reverse('advisor_profile'))


@login_required
def deactivate_profile(request):
    """
    View to deactivate profile.
    If profile is deactivated / activated, send a feedback.
    """
    profile = get_advisor_by_request_user(request)

    if profile.active == 1:

        profile.active = 0
        profile.save()

        advisor_deactivated_email(profile)

        messages.success(
            request,
            'Your profile has been deactivated.'
            )

    else:

        profile.active = 1
        profile.save()

        advisor_activated_email(profile)

        messages.success(
            request,
            'Your profile has been activated.'
        )

    return redirect('advisor_profile')


@login_required
def clients_list(request):
    """
    View to show all of the advisor clients.
    """
    # Get advisor profile of logged in user
    advisor = get_advisor_by_request_user(request)

    # Filter matches by logged in advisor
    matches = Match.objects.filter(advisor=advisor)
    matches_count = matches.count()

    context = {
        'matches_count': matches_count,
        'matches': matches
    }

    return render(request, 'advisors/clients.html', context)


@login_required
def seeker_profile(request, match_id):
    """
    Show the seekers details together with the messages.
    Show the consultation form and the message form.
    """
    # Get seeker details
    match = get_object_or_404(Match, id=match_id)
    notes = Message.objects.filter(match=match)
    consultations = Consultation.objects.filter(match=match)

    # Combine notes and consultations in 1 iterable list for template
    elements = list(chain(notes, consultations))

    # Hide consultation scheduling form
    # if there is a non confirmed consultation
    hide_consultation_form = find_uncorfirmed_consultation(consultations)

    if request.method == 'POST':

        if 'consultation' not in request.POST:
            message_form = MessageForm(data=request.POST)

            # If message form is valid get user id and save
            if message_form.is_valid():

                user = request.user
                message_form.instance.match = match
                message_form.instance.user = request.user
                message_form.save()

                messages.success(
                    request,
                    'You have sent a message successfully. \
                        Your client will receive an email.'
                )

                # Email last message to advisor
                # Get all messages by logged in user
                messages_sent = Message.objects.filter(user=user)

                # Get last message for logged in user by created_on and send
                last_message = messages_sent.latest('created_on')

                email_note_to_seeker(last_message)

            else:
                message_form = MessageForm()

            return redirect(reverse(
                'client_profile', args=[match.id]
            ))

        elif 'consultation' in request.POST:

            consultation_form = ConsultationForm(data=request.POST)

            create_consultation(consultation_form, match, request)

            return redirect(reverse(
                'client_profile', args=[match.id]
            ))

    context = {
        'match': match,
        'notes': notes,
        'consultations': consultations,
        'message_form': MessageForm,
        'consultation_form': ConsultationForm,
        'page_title': f'{ match.seeker }',
        'elements': elements,
        'hide_consultation_form': hide_consultation_form
        }

    return render(request, 'advisors/client-profile.html', context)


@login_required
def consultation_list(request):
    """
    Render all the consultations the advisor have scheduled.
    Order by date.
    """
    get_advisor_profile = get_advisor_by_request_user(request)

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

    consultation_cancelled(consultation)
    consultation.delete()
    messages.success(request, 'The consultation has been deleted.')

    return redirect('consultations')


@login_required
def client_delete_consultation(request, consultation_id, match_id):
    """
    Delete consultation and show message.
    """
    find_consultation = Consultation.objects.filter(
        match=match_id,
    )
    consultation = get_object_or_404(
        find_consultation,
        id=consultation_id
    )

    consultation_cancelled(consultation)
    consultation.delete()

    messages.success(request, 'The consultation has been deleted.')

    return redirect(reverse('client_profile', kwargs={'match_id': match_id}))
