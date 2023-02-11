from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SeekerSignupForm
from .models import SeekerUserProfile, User


@login_required
def seeker_signup(request):

    """
    View to let an seeker signup. Takes the form it is valid
    and if so save the objects in the related models.

    If the seeker profile is created, send a feedback.
    """

    if request.method == 'POST':
        form = SeekerSignupForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Signup completed.'
                )

            return redirect('signup')

    messages.error(request, 'Signup not completed. Try again.')

    form = SeekerSignupForm()

    context = {
        'form': form,
        'page_title': 'Advice Seeker Signup'
    }
    return render(request, 'seekers/signup.html', context)


@login_required
def seeker_profile(request):

    """
    seeker_profile view for profile.html.
    Render all the business details related to an advisor.
    """

    user = request.user
    queryset = SeekerUserProfile.objects
    profile = get_object_or_404(queryset, user=user)

    form = SeekerSignupForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
        'page_title': 'profile'
    }

    return render(request, 'seekers/profile.html', context)
