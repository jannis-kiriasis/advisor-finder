from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def _consultation_confirmed_email_advisor(order):
    """
    Send email to advisor with details of the consultation confirmed.
    """
    email = order.consultation.match.advisor.user.email
    subject = 'Consultation confirmed'
    body = render_to_string(
        'checkout/emails/consultation-confirmed-advisor.txt',
        {'order': order})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )


def _consultation_confirmed_email_seeker(order):
    """
    Send email to seeker with details of the consultation confirmed.
    """
    email = order.seeker.user.email
    subject = 'Consultation and payment confirmed'
    body = render_to_string(
        'checkout/emails/consultation-confirmation-seeker.txt',
        {'order': order})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )


def _send_payment_failed_email(order):
    """
    Send email to seeker when payment fails.
    """
    email = order.seeker.user.email
    subject = 'Payment failed - order not created'
    body = render_to_string(
        'checkout/emails/payment-failed.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )
