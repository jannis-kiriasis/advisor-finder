from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from .models import Match

import random
from random import shuffle


def save_match(advisor, seeker):

    """
    Save the matched in a model/
    """

    match = Match.objects.create(
        advisor=advisor,
        seeker=seeker
    )

    match.save()


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

    advisor = random.choice(filter_advisors)

    # Query all the advisors that specialise in the seeker need.
    # Return the queryset in random order

    other_advisors = list(
        AdvisorUserProfile.objects.filter(specialisation=seeker.need)
    )

    # other_advisors = AdvisorUserProfile.objects.all()
    shuffle(other_advisors)

    save_match(advisor, seeker)

    context = {
        'seeker': seeker,
        'advisor': advisor,
        'other_advisors': other_advisors,
    }

    return render(request, 'matches/match.html', context)
