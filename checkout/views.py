from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .forms import OrderForm
from seekers.models import SeekerUserProfile
from matches.models import Match
from consultations.models import Consultation

import stripe


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get the seeker profile
    get_seeker_profile = get_object_or_404(SeekerUserProfile, user=request.user)

    # Get the seeker matches (it's 1 only)
    get_all_matches = Match.objects.filter(seeker=get_seeker_profile)

    # Get latest consultation schedule of the match if it exisits.
    # If it doesn't exist redirect user to chat.
    try:
        consultation = Consultation.objects.filter(
            match__id__in=get_all_matches
            ).latest('created')
    except Consultation.DoesNotExist:
        message.error(request, ("Consultation doesn't exist."))

        return redirect('advisor')

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order_form.instance.consultation = consultation
            order_form.instance.fee = total
            order_form.instance.grand_total = grand_total

            order = order_form.save()

            total = order.fee
            stripe_total = round(total * 100)

            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))

        else:

            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    elif request.method == 'GET':

        total = consultation.price

        af_fee = total * 5 / 100
        grand_total = total + af_fee

        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email
        }

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
