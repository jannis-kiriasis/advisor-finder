from advisors.models import AdvisorUserProfile
from django.shortcuts import get_object_or_404
from seekers.models import SeekerUserProfile


def get_advisor_by_request_user(request):
    """
    Get the advisor profile by the request.user.
    """
    profile = get_object_or_404(AdvisorUserProfile, user=request.user)
    return profile


def get_seeker_by_request_user(request):
    """
    Get the seeker profile by the request.user.
    """
    seeker_profile = get_object_or_404(SeekerUserProfile, user=request.user)
    return seeker_profile
