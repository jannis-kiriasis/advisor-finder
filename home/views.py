from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserTypeForm
from .models import UserProfile


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

    messages.error(request, 'Signup not completed. Try again.')

    form = UserTypeForm()

    context = {
        'form': form,
        'page_title': 'Are you Advisor or Seeker?'
    }

    # if the logged in user has a user profile already, complete the advisor or
    # the seeker signup process

    if UserProfile.objects.filter(user=request.user).exists():

        user = UserProfile.objects.get(user=request.user)

        if user.user_type == 0:
            return redirect('advisor_signup')

        elif user.user_type == 1:
            return redirect('seeker_signup')

    # if the logged in user doesn't have a profile, render the
    # /advisor-or-seeker/ template to choose a user type.

    else:
        return render(request, 'home/advisor-or-seeker.html', context)
