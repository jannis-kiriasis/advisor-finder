from django.contrib import messages
from django.conf import settings

from consultations.models import Consultation
from matches.models import Match

import stripe


def order_paid(order):
    """
    Mark order object as paid
    after successful payment Stripe webhook is received.
    """
    if order.paid is False:
        order.paid = True
        order.save()


def save_order_form(order_form, request, total, af_fee, grand_total):
    """
    Fill all the order object fields.
    Save order form in checkout view after validation.
    """
    order_form.instance.fee = total
    order_form.instance.af_fee = af_fee
    order_form.instance.grand_total = grand_total

    stripe_total = round(total * 100)
    order_form.instance.stripe_total = stripe_total

    order = order_form.save(commit=False)
    pid = request.POST.get('client_secret').split('_secret')[0]
    order.stripe_pid = pid
    order.save()

    return order


def checkout_data_for_get_request(
        total, get_seeker_profile, request, consultation, stripe_secret_key):
    """
    Get all the data needed for the checkout view GET request.
    """
    stripe_total = round(total * 100)

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    data = {
        'name': get_seeker_profile.user.first_name,
        'last_name': get_seeker_profile.user.last_name,
        'email': get_seeker_profile.user.email,
        'postcode': get_seeker_profile.postcode,
        'town_or_city': get_seeker_profile.town_or_city,
        'street_address': get_seeker_profile.street_address,
        'consultation': consultation,
        'seeker': get_seeker_profile
    }

    return stripe_total, intent, data
