from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def email_note_to_advisor(last_message):
    """
    Advisor receives an email when seeker send a message.
    """
    subject = 'Advice Found: you have a new message'
    message = render_to_string(
        'seekers/emails/email-note-to-advisor.txt',
        {'last_message': last_message})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.advisor.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
