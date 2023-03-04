from django.shortcuts import get_object_or_404
from checkout.emails import consultation_confirmed_email, payment_failed_email
from checkout.emails import payment_succeeded_email


def confirm_consultation(order):
    get_consultation = order.consultation

    get_consultation.status = 1
    get_consultation.save()

    consultation_confirmed_email(order)
    payment_succeeded_email(order)
