import stripe

from django.contrib import messages
from django.conf import settings

from consultations.models import Consultation
from matches.models import Match


def order_paid(order):
    """
    Mark order object as paid
    after successful payment Stripe webhook is received.
    """
    if order.paid is False:
        order.paid = True
        order.save()


def show_fees(consultation):
    """
    Show consultation fee breakdown in checkout view.
    """
    total = consultation.price

    af_fee = total * 5 / 100
    grand_total = total + af_fee

    return total, af_fee, grand_total


def get_seeker_unconfirmed_consultation(get_seeker_profile):
    """
    Get any non confirmed consultation (not paid). It can't be more than 1.
    If it doesn't exist, redirect seeker to the advisor page.
    """

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

    return get_all_matches, consultation


def save_order_form(order_form, request):
    """
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


def save_POST_data_in_request_session(request):
    """
    Save checkout request.POST data in session request.
    """
    request.session['save_consultation'] = 'save-consultation' in request.POST
    request.session['save_seeker'] = 'save-seeker' in request.POST
    request.session['save_last_name'] = 'save-last-name' in request.POST


def checkout_data_for_get_request(
        total, get_seeker_profile, request, consultation):
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
