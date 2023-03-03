from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SeekerSignupForm
from .models import SeekerUserProfile, User
from django.contrib.auth import logout
from matches.models import Match, Message
from .forms import MessageForm
from .emails import email_note_to_advisor
from consultations.models import Consultation
from itertools import chain


@login_required
def seeker_signup(request):

    """
    View to let an seeker signup. Takes the form it is valid
    and if so save the objects in the related models.

    If the seeker profile is created, send a feedback.
    """

    if request.method == 'POST':
        form = SeekerSignupForm(request.POST)

        if form.is_valid():

            form.instance.user = request.user
            form.save()

            messages.success(
                request,
                'Signup completed.'
                )

            return redirect('seeker_signup')

    messages.error(request, 'Signup not completed. Try again.')

    form = SeekerSignupForm()

    context = {
        'form': form
    }
    return render(request, 'seekers/signup.html', context)


@login_required
def seeker_profile(request):

    """
    seeker_profile view for profile.html.
    Render all the business details related to an advisor.
    """

    user = request.user
    queryset = SeekerUserProfile.objects
    profile = get_object_or_404(queryset, user=user)

    form = SeekerSignupForm(instance=profile)

    if request.method == 'POST':

        form = SeekerSignupForm(request.POST, instance=profile)

        if form.is_valid():

            profile = form.save()

            messages.success(
                request,
                'Your profile has been updated.'
            )

            return redirect('seeker_profile')

        else:

            messages.error(
                request,
                "Your update request didn't go through. Try again."
            )

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.user.first_name} {profile.user.last_name}'
    }

    return render(request, 'seekers/profile.html', context)


@login_required
def delete_profile(request):
    """
    View to delete profile.
    If profile is deleted, send a feedback.
    """

    user = request.user
    profile = get_object_or_404(SeekerUserProfile, user=user)
    profile.delete()
    messages.success(request, 'Your profile has been deleted.')
    logout(request)

    return redirect('')


@login_required
def advisor_profile(request):

    """
    View to show advisor profile to the seeker.
    """

    # Get advisor profile of logged in user

    user = request.user
    seeker = get_object_or_404(SeekerUserProfile, user=user)

    matches = Match.objects
    match = get_object_or_404(matches, seeker=seeker)

    notes = Message.objects.filter(match=match)
    consultations = Consultation.objects.filter(match=match)

    # Combine notes and consultations in 1 iterable list for template

    elements = list(chain(notes, consultations))

    if request.method == 'POST':
        message_form = MessageForm(data=request.POST)

        # If message form is valid get user id and save

        if message_form.is_valid():

            user = request.user
            seeker_profile = SeekerUserProfile.objects.filter(user=user)
            message_form.instance.match = match
            message_form.instance.user = request.user

            message_form.save()

            messages.success(request, 'You have sent a message successfully. You advisor will reply as soon as possible.')

            # Email last message to advisor

            # Get all messages by logged in user
            messages_sent = Message.objects.filter(user=user)

            # Get last message for logged in user by created_on and send
            last_message = messages_sent.latest('created_on')
            email_note_to_advisor(last_message)

            return redirect(reverse('advisor'))

        else:
            message_form = MessageForm()

    context = {
        'match': match,
        'message_form': MessageForm,
        'elements': elements
    }

    return render(request, 'seekers/advisor.html', context)
