from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SeekerSignupForm
from .models import SeekerUserProfile, User
from django.contrib.auth import logout


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

            form.instance.user = request.user
            form.save()

            messages.success(
                request,
                'Signup completed.'
                )

            return redirect('seeker_signup')

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

    if request.method == 'POST':

        form = SeekerSignupForm(request.POST, instance=profile)

        if form.is_valid():

            profile = form.save()

            messages.success(
                request,
                'Your profile has been updated.'
            )

            return redirect('seeker_profile')

        else:

            messages.error(
                request,
                "Your update request didn't go through. Try again."
            )

    context = {
        'profile': profile,
        'form': form,
        'page_title': f'{profile.user.first_name} {profile.user.last_name}'
    }

    return render(request, 'seekers/profile.html', context)


@login_required
def delete_profile(request):
    """
    View to delete profile.
    If profile is deleted, send a feedback.
    """

    user = request.user
    profile = get_object_or_404(SeekerUserProfile, user=user)
    profile.delete()
    messages.success(request, 'Your profile has been deleted.')
    logout(request)

    return redirect('')
