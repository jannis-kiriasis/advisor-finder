from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

from advisor_finder.utils import get_seeker_by_request_user
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from seekers.forms import SeekerSignupForm

from .models import Match
from .emails import new_client_email

import random
from random import shuffle


@login_required
def match(request):
    """
    View to show best match.
    """
    # Get seekers profile of logged in user
    seeker = get_seeker_by_request_user(request)

    # If seeker is already matched, go to advisor page
    find_match = False

    if not find_match:
        find_match = Match.objects.filter(
            seeker=seeker
        )

    if find_match:
        return redirect('advisor')

    # Filter advisors by approved and active statuses and then location
    # and specialisation. Finally, take a random object from the queryset
    advisor_objects = AdvisorUserProfile.objects
    filter_advisors = advisor_objects.filter(
        approved=1,
        active=1,
        town_or_city=seeker.town_or_city,
        specialisation=seeker.need
    )
    if not filter_advisors:
        filter_advisors = advisor_objects.filter(
            approved=1,
            active=1,
            specialisation=seeker.need
        )
        if not filter_advisors:

            filter_advisors = advisor_objects.filter(
                approved=1,
                active=1,
            )
            if not filter_advisors:
                messages.warning(
                    request,
                    'There are no advisors available currently. \
                    Try again later.'
                )
                logout(request)
                return redirect('account_login')

    advisor = random.choice(filter_advisors)

    # Query all the advisors that specialise in the seeker need.
    # Return the queryset in random order

    other_advisors = list(
        AdvisorUserProfile.objects.filter(specialisation=seeker.need)
    )

    # other_advisors = AdvisorUserProfile.objects.all()
    shuffle(other_advisors)

    context = {
        'seeker': seeker,
        'best_advisor': advisor,
        'other_advisors': other_advisors,
    }

    return render(request, 'matches/match.html', context)


@login_required
def create_match(request, *arg, **kwargs):
    """
    Save the match after defensive design confirmation.
    Make sure seekers doesn't have an adviser yet.
    """
    # get view url
    url = request.path

    # The digits after the last '/' are equal to the advisor_id choosen
    advisor_id = url.split('select-advisor/', 1)[1]

    user = request.user
    advisor = AdvisorUserProfile(id=advisor_id)
    seeker = get_seeker_by_request_user(request)

    # Check if the seeker already has an advisor, if not create the match
    if Match.objects.filter(seeker=seeker):
        messages.warning(request, 'You already have an advisor.')
    else:
        match = Match.objects.create(
            advisor=advisor,
            seeker=get_object_or_404(SeekerUserProfile, user=user)
        )

        new_client_email(match)

        messages.success(
            request,
            'Great job! Send a message to your new advisor below!')

    return redirect('advisor')
