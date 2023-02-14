from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserTypeForm


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
    return render(request, 'home/advisor-or-seeker.html', context)
