from django.shortcuts import redirect, get_object_or_404

from advisor_finder.utils import get_advisor_by_request_user
from advisor_finder.utils import get_seeker_by_request_user
from advisor_finder.utils import get_user_profile_by_request_user
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from matches.models import Match

from .models import UserProfile


def choose_the_page_to_return_to_user(request):
    """
    This logic is to figure out what page to return to the user depending on:
    - whether they have a UserProfile model or not
    - whether they are advisors or seekers
    - whether they have completed the advisor / seeker signup up form or not.
    """
    # check if the logged in user has a userProfile. If not, create one
    if UserProfile.objects.filter(user=request.user).exists():

        user_profile = get_user_profile_by_request_user(request)

        # if the userProfile exists, check whether it's Advisor or Seeker
        if user_profile.user_type == 0:

            # If it's advisor, check advisor profile has been created.
            # If not, create one.
            if AdvisorUserProfile.objects.filter(user=request.user):

                # check the profile is approved. If so show clients.
                # If not, show profile
                advisor = get_advisor_by_request_user(request)

                if advisor.approved == 1:
                    return redirect('clients')
                else:
                    return redirect('advisor_profile')

            else:
                return redirect('advisor_signup')

        elif user_profile.user_type == 1:

            # If seeker profile exists,
            # check whether an advisor has been assigned

            if SeekerUserProfile.objects.filter(user=request.user):

                seeker = get_seeker_by_request_user(request)
                print(seeker)
                # If the seeker has an advisor, go to advisor page
                # if not, go to match page

                if Match.objects.filter(seeker=seeker):
                    return redirect('advisor')
                else:
                    return redirect('match')

            else:
                return redirect('seeker_signup')

