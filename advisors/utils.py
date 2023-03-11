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
