from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from matches.models import Match

from .forms import UserTypeForm
from .models import UserProfile
from .utils import choose_the_page_to_return_to_user


def index(request):
    """Return index.html page"""

    return render(request, 'home/index.html')


@login_required
def advisor_seeker(request):
    """
    Advisir signup view. Takes the form it is valid
    and if so save the objects in the related models.

    If the advisor profile is created, send a feedback.
    """
    if request.method == 'POST':
        form = UserTypeForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()

            # if Advisor return advisor signup. If seeker return seeker signup.
            if form.instance.user_type == 0:
                return redirect('advisor_signup')
            elif form.instance.user_type == 1:
                return redirect('seeker_signup')

        elif not form.is_valid():
            return redirect(reverse('choice'))

    elif request.method == 'GET':
        # function to decide what page to show to users depending on:
        # - their user profile exists or not
        # - their user_type
        # - they have completed the advisor / seeker signup form
        user_profile = UserProfile.objects.filter(user=request.user)

        if user_profile:
            return choose_the_page_to_return_to_user(request)

        form = UserTypeForm()

        context = {
            'form': form,
            'page_title': 'Are you Advisor or Seeker?'
        }

    return render(request, 'home/advisor-or-seeker.html', context)
