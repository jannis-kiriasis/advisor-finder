from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from seekers.forms import SeekerSignupForm
from .models import Match
from django.contrib import messages
from django.contrib.auth.models import User


import random
from random import shuffle


@login_required
def match(request):

    """
    View to show best match.
    """

    # Get seekers profile of logged in user

    user = request.user
    seeker_objects = SeekerUserProfile.objects
    seeker = get_object_or_404(seeker_objects, user=user)

    # Filter advisors by approved and active statuses and then location 
    # and specialisation. Finally, take a random object from the queryset

    advisor_objects = AdvisorUserProfile.objects
    filter_advisors = advisor_objects.filter(
        approved=1,
        active=1,
        town_or_city=seeker.town_or_city,
        specialisation=seeker.need
    )

    if random.choice(filter_advisors):
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

    else:
        messages.warning(
            request,
            'There are no advisors available currently, try again later.'
        )
        return redirect('seeker_profile')


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
    seeker = get_object_or_404(SeekerUserProfile, user=user)

    # Check if the seeker already has an advisor, if not create the match
    if Match.objects.filter(seeker=seeker):
        messages.warning(request, 'You already have an advisor.')
    else:
        match = Match.objects.create(
            advisor=advisor,
            seeker=get_object_or_404(SeekerUserProfile, user=user)
        )

    return redirect('advisor')
