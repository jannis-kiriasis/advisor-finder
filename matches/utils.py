from django.contrib import messages
from advisor_finder.utils import get_advisor_by_request_user
import random


def best_match_logic(request):
    """
    Find the best match for the seeker.
    first look to match the parameters:
    1. advisor approved, advisor active, same need, same location. If not:
    2. advisor approved, advisor active, same need. If not:
    3. advisor approved, advisor active. If not:
    4. Log user out and show come back later message.
    """
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
                    'There are no advisors available currently, \
                    try again later.'
                )
                logout(request)

    advisor = random.choice(filter_advisors)

    return advisor
