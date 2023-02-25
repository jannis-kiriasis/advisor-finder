from django.conf import settings
from django.core.mail import send_mail


def email_note_to_advisor(message_form):

    """
    Advisor receives an email when seeker send a message.
    """

    subject = 'Advice Found: you have a new message'
    message = f'From: {message_form.user.first_name} {message_form.user.last_name}. Message: {message_form.body}. Sent on {message_form.created_on}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [{message_form.match.advisor.user.email}, ]
    send_mail(subject, message, email_from, recipient_list)
