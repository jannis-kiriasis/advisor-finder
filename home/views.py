from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):

    """Return index.html page"""

    return render(request, 'home/index.html')


@login_required
def advisor_seeker(request):

    """Return advisor or seeker page"""

    context = {
        'page_title': 'Are you Advisor or Seeker?'
    }

    return render(request, 'home/advisor-or-seeker.html', context)
