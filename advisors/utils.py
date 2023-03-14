from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile_status_messasge(request, profile):
    if profile.approved == 0:
        messages.warning(
            request,
            "Your profile is pending approval. \
            You'll be notified once approved."
        )
    if profile.approved == 1:
        messages.success(
            request,
            'Your profile is approved. You can receive contact requests.'
        )
    if profile.approved == 2:
        messages.error(
            request, 'Your profile has not approved. \
            Check the information you have submitted and try again.'
        )


def find_uncorfirmed_consultation(consultations):
    """
    Find uncorfirmed consultations. If there are uncorfimed consultations,
    don't show consultation scheduling form on seeker_profile view GET request.
    """
    hide_consultation_form = False
    consultation_not_confirmed = False

    if hide_consultation_form is False:
        try:
            consultation_not_confirmed = consultations.filter(status=0)
        except Exception:
            pass

        if consultation_not_confirmed:
            hide_consultation_form = True

    return hide_consultation_form
