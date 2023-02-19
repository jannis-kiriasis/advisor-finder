from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdvisorSignupForm
from .models import AdvisorUserProfile, User
from .emails import advisor_to_approve_email, advisor_deactivated_email, advisor_activated_email


@login_required
def advisor_signup(request):

    """
    View to let an advisor signup. Takes the form it is valid
    and if so save the objects in the related models.

    If the advisor profile is created, send a feedback.
    """

    if request.method == 'POST':
        form = AdvisorSignupForm(request.POST)

        if form.is_valid():

            form.instance.user = request.user
            form.save()

            messages.success(
                request,
                'Signup completed. Now wait for Advice Found profile check.'
                )

            queryset = AdvisorUserProfile.objects
            profile = get_object_or_404(queryset, user=request.user)

            advisor_to_approve_email(profile)

            return redirect('advisor_signup')

        else:
            messages.error(request, 'Signup not completed. Try again.')

    form = AdvisorSignupForm()

    context = {
        'form': form,
        'page_title': 'Financial Advisor Signup'
    }
    return render(request, 'advisors/signup.html', context)


@login_required
def advisor_profile(request):

    """
    advisor_profile view for profile.html.
    Render all the business details related to an advisor.
    """

    user = request.user
    queryset = AdvisorUserProfile.objects
    profile = get_object_or_404(queryset, user=user)

    form = AdvisorSignupForm(instance=profile)

    if request.method == 'POST':

        form = AdvisorSignupForm(request.POST, instance=profile)

        if form.is_valid():

            profile.approved = 0
            profile = form.save()

            messages.success(
                request,
                'Your update request has been forwarded. Now wait for Advice Found review.'
            )

            advisor_to_approve_email(profile)

            return redirect('advisor_profile')

        else:

            messages.error(
                request,
                "Your update request didn't go through. Try again."
            )

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.business_name} profile'
    }

    return render(request, 'advisors/profile.html', context)


@login_required
def deactivate_profile(request):
    """
    View to deactivate profile.
    If profile is deactivated / activated, send a feedback.
    """

    user = request.user
    profile = get_object_or_404(AdvisorUserProfile, user=user)

    if profile.active == 1:

        profile.active = 0
        profile.save()

        advisor_deactivated_email(user, profile)

        messages.success(request, 'Your profile has been deactivated.')

    else:

        profile.active = 1
        profile.save()

        advisor_activated_email(user, profile)

        messages.success(request, 'Your profile has been activated.')

    return redirect('advisor_profile')
