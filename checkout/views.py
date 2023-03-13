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
from .utils import save_order_form
from .utils import checkout_data_for_get_request

import json
import stripe


@require_POST
def cache_checkout_data(request):
    """
    Save the following information in request.POST.
    """
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
    """
    View to pay for a consultation = checkout.

    The GET request shows all of the order details prefilled in the order form.
    The POST request send a payment intent to Stripe.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get the seeker profile
    get_seeker_profile = get_object_or_404(
        SeekerUserProfile,
        user=request.user
    )

    # Get the seeker matches (it's 1 only)
    get_all_matches = Match.objects.filter(seeker=get_seeker_profile)

    # Get latest consultation schedule of the match if it exisits.
    # If it doesn't exist redirect user to chat.
    try:
        consultation = Consultation.objects.get(
            match__id__in=get_all_matches,
            status=0
            )
    except Consultation.DoesNotExist:
        message.error(request, ("Consultation doesn't exist."))

        return redirect('advisor')

    total = consultation.price

    af_fee = total * 5 / 100
    grand_total = total + af_fee

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order = save_order_form(
                order_form, request, total, af_fee, grand_total)

            request.session[
                'save_consultation'] = 'save-consultation' in request.POST
            request.session[
                'save_seeker'] = 'save-seeker' in request.POST
            request.session[
                'save_last_name'] = 'save-last-name' in request.POST

            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))

        else:

            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    elif request.method == 'GET':

        stripe_total, intent, data = checkout_data_for_get_request(
            total, get_seeker_profile, request, consultation, stripe_secret_key
        )

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
    Handle successfullt checkouts.
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
