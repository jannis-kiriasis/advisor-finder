from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def new_client_email(match):
    """
    Message the advisor with the details of the new client.
    """
    subject = 'Advice Found: you have a new client'
    message = render_to_string(
        'matches/emails/new-client-email.txt',
        {'match': match})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [match.advisor.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
