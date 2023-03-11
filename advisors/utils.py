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


def save_advisor_updates_in_request_session(request):
    """
    Save the advisor updated details in the request session to pass to the
    update advisor view.
    """
    request.session[
        'save_business_name'
        ] = 'save_business_name' in request.POST
    request.session[
        'save_business_description'
        ] = 'save_business_description' in request.POST
    request.session[
        'save_specialisation'
        ] = 'save_specialisation' in request.POST
    request.session[
        'save_postcode'
        ] = 'save_postcode' in request.POST
    request.session[
        'save_street_address'
        ] = 'save_street_address' in request.POST
    request.session[
        'save_town_or_city'
        ] = 'save_town_or_city' in request.POST
    request.session[
        'save_registration_number'
        ] = 'save_registration_number' in request.POST


def find_uncorfirmed_consutltation(consultations):
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
