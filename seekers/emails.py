from django.conf import settings
from django.core.mail import send_mail


def email_note_to_advisor(last_message):
    """
    Advisor receives an email when seeker send a message.
    """
    subject = 'Advice Found: you have a new message'
    message = f'From: {last_message.user.first_name} {last_message.user.last_name}.\
        Message: {last_message.body}.\
        Sent on {last_message.created_on}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [last_message.match.advisor.user.email, ]
    send_mail(subject, message, email_from, recipient_list)
