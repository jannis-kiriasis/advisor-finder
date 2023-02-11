from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdvisorSignupForm
from .models import AdvisorUserProfile, User


def advisor_signup(request):

    """
    View to let an advisor signup. Takes the form it is valid
    and if so save the objects in the related models.

    If the advisor profile is created, send a feedback.
    """

    if request.method == 'POST':
        form = AdvisorSignupForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Signup completed. Now wait for Advice Found profile check.'
                )

            return redirect('advisor_signup')

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

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.business_name} profile'
    }

    return render(request, 'advisors/profile.html', context)
