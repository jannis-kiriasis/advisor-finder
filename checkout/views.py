from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from advisor_finder.utils import get_seeker_by_request_user
from seekers.models import SeekerUserProfile
from matches.models import Match
from consultations.models import Consultation
from home.models import UserProfile

from .forms import OrderForm
from .models import Order
from .utils import show_fees, get_seeker_unconfirmed_consultation
from .utils import save_order_form, save_POST_data_in_request_session
from .utils import checkout_data_for_get_request


import json
import stripe


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'save_consultation': request.POST.get('save_consultation'),
            'save_seeker': request.POST.get('save_seeker'),
            'save_last_name': request.POST.get('save_last_name')
        })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get the seeker profile
    get_seeker_profile = get_seeker_by_request_user(request)

    # Get seeker unconfirmed consultation
    consultation, get_all_matches = get_seeker_unconfirmed_consultation(
        get_seeker_profile
        )

    # Calculate fees
    total, af_fee, grand_total = show_fees(consultation)

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order = save_order_form(order_form, request)

            save_POST_data_in_request_session(request)

            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))

        else:

            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    elif request.method == 'GET':

        stripe_total, intent, data = checkout_data_for_get_request(
            get_seeker_profile, total, consultation, request)

        order_form = OrderForm(data)

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'page_title': 'Checkout',
            'fee': total,
            'af_fee': af_fee,
            'grand_total': grand_total
        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successfullt checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout-success.html', context)
