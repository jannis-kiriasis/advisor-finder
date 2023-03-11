from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User

from advisor_finder.utils import get_seeker_by_request_user
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from seekers.forms import SeekerSignupForm

from .models import Match
from .utils import best_match_logic

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
    advisor = best_match_logic(request)

    # Query all the advisors that specialise in the seeker need.
    # Return the queryset in random order
    other_advisors = list(
        AdvisorUserProfile.objects.filter(specialisation=seeker.need)
    )

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

    return redirect('advisor')
