from django.shortcuts import render, redirect, get_object_or_404, reverse
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
from home.models import Location, Specialisation


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

            return redirect('match')

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
            request.session[
                'save_need'
                ] = 'save_need' in request.POST
            request.session[
                'save_postcode'
                ] = 'save_postcode' in request.POST
            request.session[
                'save_town_or_city'
                ] = 'save_town_or_city' in request.POST
            request.session[
                'save_street_address'
                ] = 'save_street_address' in request.POST

            return redirect(reverse(
                'seeker_update',
            ))

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.user.first_name} {profile.user.last_name}'
    }

    return render(request, 'seekers/profile.html', context)


@login_required
def update_profile(request):
    """
    View to delete profile.
    If profile is deleted, send a feedback.
    """

    saved_need = request.POST['save_need']
    saved_postcode = request.POST['save_postcode']
    saved_street_address = request.POST['save_street_address']
    saved_town_or_city = request.POST['save_town_or_city']

    print(saved_town_or_city)

    specialisation = get_object_or_404(
        Specialisation,
        type=saved_need
    )

    town_or_city = Location.objects.filter(
        city=saved_town_or_city
    ).latest('city')

    profile = get_object_or_404(
        SeekerUserProfile,
        user=request.user
        )

    profile.need = specialisation
    profile.postcode = saved_postcode
    profile.street_address = saved_street_address
    profile.town_or_city = town_or_city
    new_profile = profile.save()

    print(profile.need)
    messages.success(
        request,
        'Your profile has been updated.'
    )

    return redirect('seeker_profile')


@login_required
def delete_profile(request):
    """
    View to delete profile.
    If profile is deleted, send a feedback.
    """
    profile = get_object_or_404(SeekerUserProfile, user=request.user)
    profile.delete()

    user = get_object_or_404(User, id=request.user.id)
    user.delete()

    messages.success(request, 'Your profile has been deleted.')
    logout(request)

    return redirect('home')


@login_required
def advisor_profile(request):

    """
    View to show advisor profile to the seeker.
    """

    # Get advisor profile of logged in user

    user = request.user
    seeker = get_object_or_404(SeekerUserProfile, user=user)
    match = False
    try:
        matches = Match.objects
        match = get_object_or_404(matches, seeker=seeker)
    except:
        pass

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
