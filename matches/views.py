from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile


@login_required
def match(request):

    """
    View to show best match.
    """

    user = request.user
    seeker_objects = SeekerUserProfile.objects
    seeker = get_object_or_404(seeker_objects, user=user)

    advisor_objects = AdvisorUserProfile.objects
    filter_advisors = advisor_objects.filter(
        approved=1,
        active=1,
        town_or_city=seeker.town_or_city,
        specialisation=seeker.need
    )

    advisor = filter_advisors.last()

    context = {
        'seeker': seeker,
        'advisor': advisor,
        'page_title': 'Dashboard'
    }

    return render(request, 'matches/match.html', context)
