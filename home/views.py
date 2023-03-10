from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserTypeForm
from .models import UserProfile
from advisors.models import AdvisorUserProfile
from seekers.models import SeekerUserProfile
from matches.models import Match


def index(request):
    """Return index.html page"""

    return render(request, 'home/index.html')


@login_required
def advisor_seeker(request):

    """
    View to let an advisor signup. Takes the form it is valid
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

        else:
            messages.error(request, 'Signup not completed. Try again.')
            return redirect('choice')

    else: 

        # check if the logged in user has a userProfile. If not, create one

        if UserProfile.objects.get(user=request.user).exists():

            user_profile = UserProfile.objects.get(user=request.user)

            # if the userProfile exists, check whether it's Advisor or Seeker
            if user_profile.user_type == 0:

                # If it's advisor, check advisor profile has been created.
                # If not, create one.
                if AdvisorUserProfile.objects.get(user=request.user).exists():

                    # check the profile is approved. If so show clients.
                    # If not, show profile
                    advisor = AdvisorUserProfile.objects.get(user=request.user)

                    if advisor.approved == 1:
                        return redirect('clients')
                    else:
                        return redirect('advisor_profile')

                else:
                    return redirect('advisor_signup')

            elif user_profile.user_type == 1:

                # If seeker profile exists,
                # check whether an advisor has been assigned

                if SeekerUserProfile.objects.filter(user=request.user).exists():

                    seeker = SeekerUserProfile.objects.get(user=request.user)

                    # If the seeker has an advisor, go to advisor page
                    # if not, go to match page

                    if Match.objects.filter(seeker=seeker):
                        return redirect('advisor')
                    else:
                        return redirect('match')

                else:
                    return redirect('seeker_signup')

    form = UserTypeForm()

    context = {
        'form': form,
        'page_title': 'Are you Advisor or Seeker?'
    }

    return render(request, 'home/advisor-or-seeker.html', context)
