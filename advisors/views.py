from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdvisorSignupForm


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

            messages.info(
                request,
                'Signup completed. Now wait for Advice Found profile check.'
                )

            return redirect('signup')

    messages.error(request, 'Signup not completed. Try again.')

    form = AdvisorSignupForm()

    context = {
        'form': form,
        'page_title': 'Financial Advisor Signup'
    }
    return render(request, 'advisors/signup.html', context)
