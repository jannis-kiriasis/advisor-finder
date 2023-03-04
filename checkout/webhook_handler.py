from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from seekers.models import SeekerUserProfile
from consultations.models import Consultation
from .models import Order
from home.models import Location
from home.models import UserProfile
from consultations.services import confirm_consultation
import stripe
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        save_info = intent.metadata.save_info
        consultation = intent.metadata.save_consultation
        seeker = intent.metadata.save_seeker

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)

        # Update profile information if save_info was checked
        seeker = SeekerUserProfile.objects.get(id=seeker)
        user = User.objects.get(id=seeker.user_id)

        location = Location.objects.get(
            id=billing_details.address.city
        )

        if save_info:
            user.phone_number = billing_details.phone
            seeker.postcode = billing_details.address.postal_code
            seeker.town_or_city = location
            seeker.street_address = billing_details.address.line1
            user.save()
            seeker.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:

                order = get_object_or_404(Order, consultation=consultation)

                order_exists = True

                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        else:
            order = None
            try:

                order = Order.objects.create(
                    name=billing_details.name,
                    last_name=intent.metadata.save_last_name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address=billing_details.address.line1,
                    consultation=consultation,
                    seeker=seeker,
                    fee=consultation.price,
                    stripe_pid=pid,
                )
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

            # send_email(payment_failed)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

        # confirm_consultation(order)
        # send_email(payment_succeeded)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
