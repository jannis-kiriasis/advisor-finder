from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, get_object_or_404


from .forms import OrderForm
from seekers.models import SeekerUserProfile
from matches.models import Match
from consultations.models import Consultation

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():

            get_seeker_profile = get_object_or_404(SeekerUserProfile, user=request.user)
            get_all_matches = Match.objects.filter(seeker=get_seeker_profile)

            consultation = Consultation.objects.filter(
                match__id__in=get_all_matches
                ).latest('created')

            order_form.instance.consultation = consultation

            order = order_form.save()

            total = consultation.price
            stripe_total = round(total * 100)

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse(
                'checkout_success', args=[order.order_number]
            ))

        else:

            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:

        get_seeker_profile = get_object_or_404(SeekerUserProfile, user=request.user)

        get_all_matches = Match.objects.filter(seeker=get_seeker_profile)

        consultation = Consultation.objects.filter(
            match__id__in=get_all_matches
            ).latest('created')

        total = consultation.price
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'page_title': 'Checkout'
    }

    return render(request, 'checkout/checkout.html', context)
